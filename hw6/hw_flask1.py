from flask import Flask

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"}
]

@app.get("/")
def home():
    return "Hello"

@app.get("/books/")
def get_books():
    books_list = "<br>".join([f"{book['id']}. <b>{book['title']}</b> by {book['author']} ({book['genre']})" for book in books])
    return f"<h2>Список книг:</h2><p>{books_list}</p>"

@app.get("/books/<int:book_id>/")
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    return f"{book['title']} by {book['author']} ({book['genre']})" if book else ("Книга не знайдена", 404)


if __name__ == '__main__':
    app.run(port=5010, debug=True)