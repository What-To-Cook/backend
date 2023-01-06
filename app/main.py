import os
from typing import (
    Any,
    Optional,
)

from fastapi import (
    Depends,
    FastAPI,
)

from app.config import CONFIG
from app.db import MongoDatabase

app = FastAPI(
    title='What To Cook?',
    description='REST API for "What To Cook?" app.',
)


async def get_db() -> MongoDatabase:  # type: ignore
    db = MongoDatabase(
        os.environ['MONGO_HOST'],
        int(os.environ['MONGO_PORT']),
        db=CONFIG.db.name,
        recipes_collection=CONFIG.db.recipes_collection,
        ingredients_collection=CONFIG.db.ingredients_collection,
    )

    try:  # noqa: WPS501
        yield db
    finally:
        db.close()


@app.get('/ingredients')
async def query_ingredients(
    db: MongoDatabase = Depends(get_db),
) -> list[str]:
    return db.query_ingredients()


@app.get('/recipes')
async def query_recipes(
    ingredients: list[str],
    allergies: Optional[list[str]] = None,
    db: MongoDatabase = Depends(get_db),
) -> list[dict[str, Any]]:
    return db.query_suitable_recipes(
        ingredients,
        allergies,
    )
