from dotenv import load_dotenv
import os

load_dotenv()

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY")

# JWT Algorithm
ALGORITHM = os.getenv("ALGORITHM")

# Token expiry times
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))