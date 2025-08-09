from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base, engine

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    chats = relationship("ChatModel", back_populates="user")


    class Config:
        orm_mode = True
        from_attributes = True


# Create the database tables
Base.metadata.create_all(bind=engine)