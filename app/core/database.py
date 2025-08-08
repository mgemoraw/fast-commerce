from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session, sessionmaker
from typing import Generator


Base = declarative_base()
engine = create_engine(
    "sqlite:///./test.db", 
    connect_args={"check_same_thread": False}  # Only for SQLite,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()