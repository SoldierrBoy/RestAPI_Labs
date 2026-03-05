from uuid import uuid4
from repository.book_repository import (
    get_all_books,
    get_book_by_id,
    add_book,
    delete_book
)


async def get_books():
    return await get_all_books()


async def get_book(book_id):
    return await get_book_by_id(book_id)


async def create_book(book_data):
    book = book_data.model_dump()
    book["id"] = uuid4()
    await add_book(book)
    return book


async def remove_book(book_id):
    return await delete_book(book_id)