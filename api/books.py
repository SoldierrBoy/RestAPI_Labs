from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from uuid import UUID

from schemas.book_schema import BookCreate, Book
from services.book_service import (
    get_books,
    get_book,
    create_book,
    remove_book
)

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[Book])
async def get_all_books(
        author: Optional[str] = Query(None),
        status: Optional[str] = Query(None),
        sort_by: Optional[str] = Query(None)
):
    books = await get_books()

    if author:
        books = [b for b in books if b["author"] == author]

    if status:
        books = [b for b in books if b["status"] == status]

    if sort_by == "title":
        books = sorted(books, key=lambda x: x["title"])

    if sort_by == "year":
        books = sorted(books, key=lambda x: x["year"])

    return books


@router.get("/{book_id}", response_model=Book)
async def get_book_by_id(book_id: UUID):
    book = await get_book(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", response_model=Book, status_code=201)
async def add_book(book: BookCreate):
    new_book = await create_book(book)
    return new_book


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: UUID):
    await remove_book(book_id)
    return