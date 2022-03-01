from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://repl:S3cretPassw0rd@localhost:5432/campdata_prod"
)
session = Session(engine)
Base = declarative_base()