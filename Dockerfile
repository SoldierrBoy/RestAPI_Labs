FROM python:3.13

WORKDIR /app

COPY . .


RUN pip install fastapi uvicorn motor python-dotenv httpx pytest

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]