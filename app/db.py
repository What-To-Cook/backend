import os
from typing import (
    Any,
    Optional,
)
from urllib.parse import quote_plus

from pymongo import MongoClient

_INGREDIENTS_KEY = 'ingredients'


# TODO: move to async driver
class MongoDatabase:
    def __init__(  # noqa: WPS211
        self,
        host: str,
        port: int,
        *,
        db: str,
        recipes_collection: str,
        ingredients_collection: str,
    ) -> None:
        self._db = db
        self._recipes_collection = recipes_collection
        self._ingredients_collection = ingredients_collection

        self._client = MongoClient(
            self._get_connection_string(
                host,
                port,
            ),
        )

    def query_ingredients(
        self,
    ) -> list[str]:
        ingredients = self._client[self._db][self._ingredients_collection].find_one()

        return sorted(ingredients[_INGREDIENTS_KEY])

    def query_suitable_recipes(
        self,
        ingredients: list[str],
        allergies: Optional[list[str]] = None,
    ) -> list[dict[str, Any]]:
        if allergies is None:
            allergies = []

        query = {
            '$and': [
                {
                    'unique_ingredients': {
                        '$not': {
                            '$elemMatch': {
                                '$nin': ingredients,
                            },
                        },
                    },
                },
                {
                    'unique_ingredients': {
                        '$nin': allergies,
                    },
                },
            ],
        }

        return list(
            self._client[self._db][self._recipes_collection].find(
                query,
                {
                    '_id': 0,
                    'unique_ingredients': 0,
                },
            ),
        )

    def close(
        self,
    ) -> None:
        self._client.close()

    @staticmethod
    def _get_connection_string(
        host: str,
        port: int,
    ) -> str:
        user = quote_plus(os.environ['MONGO_USER'])
        password = quote_plus(os.environ['MONGO_PASSWORD'])

        return f'mongodb://{user}:{password}@{host}:{port}/'  # noqa: WPS221
