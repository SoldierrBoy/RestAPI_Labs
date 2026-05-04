import httpx

MOCK_URL = "http://localhost:4010/books/"


def test_get_books_mock():
    response = httpx.get(MOCK_URL)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["title"] == "Dune"
    assert data[0]["author"] == "Frank Herbert"


def test_create_book_success_mock():
    new_book = {
        "title": "Тестова книга",
        "author": "Іван Іваненко",
        "description": "Тестовий опис для перевірки",
        "status": "available",
        "year": 2026
    }
    response = httpx.post(MOCK_URL, json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Dune Messiah"


def test_create_book_validation_error_mock():
    invalid_book = {
        "title": "Книга без автора та інших обов'язкових полів"
    }
    response = httpx.post(MOCK_URL, json=invalid_book)
    assert response.status_code == 422