from pydantic import BaseModel, Field
from typing import Optional
import strawberry



class BookCreateSchema(BaseModel):
    title: str = Field(..., title="Title of the book", max_length=100)
    author: str = Field(..., title="Author of the book", max_length=50)
    publisher: str = Field(..., title="Publisher of the book", max_length=50)
    name: Optional[str] = None


    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "publisher": "Scribner"
            }
        }
    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, publisher={self.publisher})"
