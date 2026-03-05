from models.book_model import books_db


async def get_all_books():
    return books_db


async def get_book_by_id(book_id):
    for book in books_db:
        if str(book["id"]) == str(book_id):
            return book
    return None


async def add_book(book):
    books_db.append(book)
    return book


async def delete_book(book_id):
    for book in books_db:
        if str(book["id"]) == str(book_id):
            books_db.remove(book)
            return True
    return False