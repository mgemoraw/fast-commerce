from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from fastapi import HTTPException
from . schemas import BookCreateSchema
from strawberry.fastapi import GraphQLRouter
from .models import Book


router = APIRouter()
data = []



@router.post("/book")
def add_book(book: BookCreateSchema, db:Session = Depends(get_db)):
    if not book.title or not book.author:
        raise HTTPException(status_code=400, detail="Title and author are required")
    
    new_book = Book(
        title=book.title,
        author=book.author,
        publisher=book.publisher
    )

    db.add(new_book)
    db.commit()
    return book

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books

@router.get("/book/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@router.put("/book/{book_id}")
def update_book(book_id: int, book: BookCreateSchema, db: Session = Depends
(get_db)):
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.title:
        existing_book.title = book.title
    if book.author:
        existing_book.author = book.author
    if book.publisher:
        existing_book.publisher = book.publisher
    
    db.commit()
    return existing_book    


@router.delete("/book/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}

# graphql_app = GraphQLRouter(graphql_schema, path="/graphql")
# router.include_router(graphql_app, prefix="/graphql", tags=["graphql"])