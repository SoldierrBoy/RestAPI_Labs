from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from api.books import BooksResource, BookResource

app = Flask(__name__)
api = Api(app)

swagger = Swagger(app)

# routes
api.add_resource(BooksResource, "/books/")
api.add_resource(BookResource, "/books/<string:book_id>")


@app.route("/")
def root():
    return {"message": "Library API is running"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)