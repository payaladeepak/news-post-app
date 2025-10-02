from fastapi import FastAPI

def create_app():
    app = FastAPI(title="News Post API")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()

