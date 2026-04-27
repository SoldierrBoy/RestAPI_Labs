FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install flask flask-restful flasgger pymongo pydantic pytest

CMD ["python", "main.py"]