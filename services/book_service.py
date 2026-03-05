from sqlalchemy.orm import Session
from models.book_model import BookModel
from repository.book_repository import (
    get_book,
    create_book,
    delete_book
)
from schemas.book_schema import BookCreate


async def get_books_service(db: Session, limit: int, cursor: str | None):

    query = db.query(BookModel)

    if cursor:
        query = query.filter(BookModel.id > cursor)

    books = query.order_by(BookModel.id).limit(limit).all()

    return books


async def get_book_service(db: Session, book_id: str):
    return get_book(db, book_id)


async def create_book_service(db: Session, book: BookCreate):
    return create_book(db, book)


async def remove_book_service(db: Session, book_id: str):
    return delete_book(db, book_id)