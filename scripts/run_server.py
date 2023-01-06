import uvicorn  # type: ignore

from app.config import CONFIG

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        host=CONFIG.server.host,
        port=CONFIG.server.port,
        workers=CONFIG.server.workers,
        log_level='debug',
    )
