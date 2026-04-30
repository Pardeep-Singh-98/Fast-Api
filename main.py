from fastapi import FastAPI
from database.connection import engine
from models.user import User

# user routes
from routes.user_router import router as user_router

app = FastAPI()

#create tables
User.metadata.create_all(bind=engine)  #automatically create user table


@app.get("/")
def home():
    return {"message":"API Running !"}


app.include_router(user_router)