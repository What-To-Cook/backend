FROM python:3.9.16-slim-bullseye

WORKDIR /app
ENV PYTHONPATH=/app

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir -U pip==22.0.3 wheel==0.38.4 setuptools==65.6.3 poetry==1.1.13 \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && rm -rf ~/.cache/pypoetry/cache ~/.cache/pypoetry/artifacts

COPY app/ ./app
COPY configs/ ./configs
COPY scripts/ ./scripts

CMD ["python", "-OO", "scripts/run_server.py"]
