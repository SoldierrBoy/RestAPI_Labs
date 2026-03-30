FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install flask flask-restful flasgger pymongo pydantic

CMD ["python", "main.py"]