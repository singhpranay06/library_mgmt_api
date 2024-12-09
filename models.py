from datetime import datetime

class Book:
    def __init__(self, id: int, title: str, author: str, isbn: str, publication_date: datetime):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date

class Member:
    def __init__(self, id: int, name: str, email: str, membership_date: datetime):
        self.id = id
        self.name = name
        self.email = email
        self.membership_date = membership_date

