
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .database import engine


models.Base.metadata.create_all(bind=engine)

description = """
## This is TestApp for Webtronics

"""
app = FastAPI(title="Test App",
              description=description,
              version="0.0.1",
              contact={
                  "name": "Vitaliy Kalachev",
                  "url": "https://www.linkedin.com/in/vitaliy-kalachev/",
                  "email": "vitaliy.kalachev@gmail.com",
              },)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(vote.router)
