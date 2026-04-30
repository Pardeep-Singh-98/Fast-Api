from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

## Mysql Database
# Database connection string
# Format:
# mysql+pymysql://username:password@host/database_name
#
# root         -> MySQL username
# password     -> MySQL password
# localhost    -> server address
# fastapi_db   -> database name

DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_jwt_pro"


# create_engine()
# Creates connection bridge between FastAPI and MySQL
#
# Think:
# FastAPI -----> Engine -----> MySQL
#
# This engine will be used everywhere in project
engine = create_engine(DATABASE_URL)


# sessionmaker()
# Creates DB session factory
#
# Session = temporary connection for each request
#
# Example:
# User hits /register API
# -> open session
# -> save data
# -> close session
SessionLocal = sessionmaker(
    autocommit=False,  # commit manually
    autoflush=False,   # save manually
    bind=engine        # connect using engine
)


# declarative_base()
# Parent class for all tables
#
# Every model inherits from Base
Base = declarative_base()