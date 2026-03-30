
from repository.book_repository import (
    get_books,
    get_book,
    create_book,
    delete_book
)

from schemas.book_schema import BookCreate


def get_books_service(limit, offset):
    return get_books(limit, offset)

def get_book_service(book_id: str):
    return get_book(book_id)


def create_book_service(book):
    return create_book(book)


def remove_book_service(book_id: str):
    return delete_book(book_id)