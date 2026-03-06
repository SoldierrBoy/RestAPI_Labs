from fastapi import APIRouter, HTTPException, Query
from typing import List

from schemas.book_schema import BookCreate, Book
from services.book_service import (
    get_books_service,
    get_book_service,
    create_book_service,
    remove_book_service
)

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[Book])
async def get_all_books(
        limit: int = Query(10, ge=1),
        offset: int = Query(0, ge=0)
):
    return await get_books_service(limit, offset)


@router.get("/{book_id}", response_model=Book)
async def get_book_by_id(book_id: str):

    book = await get_book_service(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", response_model=Book, status_code=201)
async def add_book(book: BookCreate):
    return await create_book_service(book)


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str):

    book = await remove_book_service(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")