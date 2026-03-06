from database.mongo import books_collection
from schemas.book_schema import BookCreate
from bson import ObjectId

async def get_books(limit: int, offset: int):

    books_cursor = books_collection.find().skip(offset).limit(limit)

    books = []

    for book in books_cursor:
        book["id"] = str(book["_id"])
        del book["_id"]
        books.append(book)

    return books


async def get_book(book_id: str):

    book = books_collection.find_one({"_id": ObjectId(book_id)})

    if not book:
        return None

    book["id"] = str(book["_id"])
    del book["_id"]

    return book


async def create_book(book: BookCreate):

    book_dict = book.model_dump()

    result = books_collection.insert_one(book_dict)

    book_dict["id"] = str(result.inserted_id)

    return book_dict


async def delete_book(book_id: str):

    book = books_collection.find_one({"_id": ObjectId(book_id)})

    if not book:
        return None

    books_collection.delete_one({"_id": ObjectId(book_id)})

    book["id"] = str(book["_id"])
    del book["_id"]

    return book