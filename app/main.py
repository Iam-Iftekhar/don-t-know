from fastapi import FastAPI
from app.routes import auth
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth System")
app.include_router(auth.router)
