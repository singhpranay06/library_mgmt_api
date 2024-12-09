from flask import Blueprint, request, jsonify
from models import Book, Member

book_routes = Blueprint('book_routes', __name__)
member_routes = Blueprint('member_routes', __name__)


books = []
members = []

# CRUD operations for books

@book_routes.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book(id=len(books) + 1, **data)
    books.append(book)
    return jsonify({'message': 'Book created successfully', 'id': book.id}), 201  

@book_routes.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.__dict__ for book in books])

@book_routes.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book.id == id), None)
    if book:
        return jsonify(book.__dict__)
    return jsonify({'message': 'Book not found'}), 404

@book_routes.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book.id == id), None)
    if book:
        data = request.get_json()
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.isbn = data.get('isbn', book.isbn)
        book.publication_date = data.get('publication_date', book.publication_date)
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404

@book_routes.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return jsonify({'message': 'Book deleted successfully'})



# CRUD operations for members

@member_routes.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    member = Member(id=len(members) + 1, **data)
    members.append(member)
    return jsonify({'message': 'Member created successfully', 'id': member.id}), 201

@member_routes.route('/members', methods=['GET'])
def get_members():
    return jsonify([member.__dict__ for member in members])

@member_routes.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = next((member for member in members if member.id == id), None)
    if member:
        return jsonify(member.__dict__)
    return jsonify({'message': 'Member not found'}), 404

@member_routes.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = next((member for member in members if member.id == id), None)
    if member:
        data = request.get_json()
        member.name = data.get('name', member.name)
        member.email = data.get('email', member.email)
        member.membership_date = data.get('membership_date', member.membership_date)
        return jsonify({'message': 'Member updated successfully'})
    return jsonify({'message': 'Member not found'}), 404

@member_routes.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    global members
    members = [member for member in members if member.id != id]
    return jsonify({'message': 'Member deleted successfully'})


# Bonus Features
@book_routes.route('/books/search', methods=['GET'])
def search_books():
    title = request.args.get('title', '')
    author = request.args.get('author', '')
    
    filtered_books = [book for book in books if title.lower() in book.title.lower() or author.lower() in book.author.lower()]
    return jsonify([book.__dict__ for book in filtered_books])