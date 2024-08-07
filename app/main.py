from fastapi import FastAPI

from app.api import router as api_router
from app.scheduler import start_scheduler, stop_scheduler

app = FastAPI(
    title="Metro",
    description="Metro test task",
    version="1.0.0",
    docs_url="/api/docs",
)


# Запускаем планировщик при старте приложения
@app.on_event("startup")
async def startup_event():
    start_scheduler()


# Останавливаем планировщик при выключении
@app.on_event("shutdown")
async def shutdown_event():
    stop_scheduler()


app.include_router(api_router)
