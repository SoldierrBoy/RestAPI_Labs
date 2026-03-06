
from repository.book_repository import (
    get_books,
    get_book,
    create_book,
    delete_book
)

from schemas.book_schema import BookCreate


async def get_books_service(limit: int, offset: int):
    return await get_books(limit, offset)


async def get_book_service(book_id: str):
    return await get_book(book_id)


async def create_book_service(book: BookCreate):
    return await create_book(book)


async def remove_book_service(book_id: str):
    return await delete_book(book_id)