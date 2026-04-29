FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn motor "pydantic[email]" python-jose[cryptography] "passlib[bcrypt]" bcrypt==4.0.1 email-validator pytest pytest-anyio httpx

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]