from fastapi import FastAPI

from app.api import router as api_router


app = FastAPI(
	title="Metro",
	description="Metro test task",
	version="1.0.0",
	docs_url="/api/docs",
)
app.include_router(api_router)
