from fastapi import FastAPI
from database.connection import engine
from models.user import User

from fastapi.middleware.cors import CORSMiddleware

# user routes
from routes.user_router import router as user_router

app = FastAPI()

# allow from local
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        # "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#create tables
User.metadata.create_all(bind=engine)  #automatically create user table


@app.get("/")
def home():
    return {"message":"API Running !"}


app.include_router(user_router)