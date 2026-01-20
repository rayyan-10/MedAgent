from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(title="Mental Health AI Agent")
#initial state
app.include_router(router)
