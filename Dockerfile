FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv httpx pytest motor

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]