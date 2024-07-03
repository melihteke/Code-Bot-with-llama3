from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book One", "author": "Author One"},
    {"id": 2, "title": "Book Two", "author": "Author Two"},
    {"id": 3, "title": "Book Three", "author": "Author Three"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"}), 200
    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

