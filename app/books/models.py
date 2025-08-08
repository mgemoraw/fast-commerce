from core.database import  engine, Base
# from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# engine = create_engine(
#     "sqlite:///./test.db",
#     echo=True, # Enable SQLAlchemy logging
#     connect_args={"check_same_thread": True}  # Only for SQLite)
# )

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    publisher = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, publisher={self.publisher})>"

    class Config:
        orm_mode = True


# Base.metadata.create_all(bind=engine)

# create the database tables
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

