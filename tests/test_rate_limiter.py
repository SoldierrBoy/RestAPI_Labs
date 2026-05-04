import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from fastapi import Depends
from main import app
from auth.auth_handler import create_tokens
from rate_limiter import rate_limit


# СТВОРЮЄМО ФЕЙКОВИЙ РОУТ ТІЛЬКИ ДЛЯ ТЕСТІВ
# Він не чіпає MongoDB, тому помилки "Event loop is closed" не буде!
@app.get("/test-rate-limit", dependencies=[Depends(rate_limit)])
async def dummy_route():
    return {"message": "passed"}


client = TestClient(app)


@pytest.fixture
def auth_token():
    # Генеруємо реальний токен для перевірки авторизованих лімітів
    token_dict = create_tokens("testuser@example.com")
    return token_dict["access_token"]


# ==========================================
# ТЕСТИ ДЛЯ АНОНІМНОГО КОРИСТУВАЧА (Ліміт: 2)
# ==========================================

@patch("rate_limiter.r.zcard", new_callable=AsyncMock)
@patch("rate_limiter.r.zremrangebyscore", new_callable=AsyncMock)
@patch("rate_limiter.r.zadd", new_callable=AsyncMock)
@patch("rate_limiter.r.expire", new_callable=AsyncMock)
def test_anonymous_under_limit(mock_expire, mock_zadd, mock_zrem, mock_zcard):
    # Імітуємо, що Redis каже: "Це лише 1-й запит"
    mock_zcard.return_value = 1

    # Звертаємося до нашого безпечного фейкового роута
    response = client.get("/test-rate-limit")
    assert response.status_code == 200


@patch("rate_limiter.r.zcard", new_callable=AsyncMock)
@patch("rate_limiter.r.zremrangebyscore", new_callable=AsyncMock)
@patch("rate_limiter.r.zadd", new_callable=AsyncMock)
@patch("rate_limiter.r.expire", new_callable=AsyncMock)
def test_anonymous_over_limit(mock_expire, mock_zadd, mock_zrem, mock_zcard):
    # Імітуємо, що Redis каже: "Це вже 2 запити" (ліміт вичерпано)
    mock_zcard.return_value = 2

    response = client.get("/test-rate-limit")
    assert response.status_code == 429
    assert response.json()["detail"] == "Too many requests"


# ===============================================
# ТЕСТИ ДЛЯ АВТОРИЗОВАНОГО КОРИСТУВАЧА (Ліміт: 10)
# ===============================================

@patch("rate_limiter.r.zcard", new_callable=AsyncMock)
@patch("rate_limiter.r.zremrangebyscore", new_callable=AsyncMock)
@patch("rate_limiter.r.zadd", new_callable=AsyncMock)
@patch("rate_limiter.r.expire", new_callable=AsyncMock)
def test_authenticated_under_limit(mock_expire, mock_zadd, mock_zrem, mock_zcard, auth_token):
    # Імітуємо, що Redis каже: "Це 9-й запит"
    mock_zcard.return_value = 9

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/test-rate-limit", headers=headers)
    assert response.status_code == 200


@patch("rate_limiter.r.zcard", new_callable=AsyncMock)
@patch("rate_limiter.r.zremrangebyscore", new_callable=AsyncMock)
@patch("rate_limiter.r.zadd", new_callable=AsyncMock)
@patch("rate_limiter.r.expire", new_callable=AsyncMock)
def test_authenticated_over_limit(mock_expire, mock_zadd, mock_zrem, mock_zcard, auth_token):
    # Імітуємо, що Redis каже: "Це вже 10 запитів" (ліміт вичерпано)
    mock_zcard.return_value = 10

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/test-rate-limit", headers=headers)
    assert response.status_code == 429
    assert response.json()["detail"] == "Too many requests"