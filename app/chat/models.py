from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base, engine


class ChatModel(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String, index=True)

    user = relationship("UserModel", back_populates="chats")

    class Config:
        orm_mode = True
        from_attributes = True


# Create the database tables
Base.metadata.create_all(bind=engine)