import unittest
from main import app  
from flask import json

class LibraryManagementSystemTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()

    def setUp(self):
        """Create initial data for books and members"""
        # Creating some initial books
        self.book_data = {
            'title': '1984',
            'author': 'George Orwell',
            'isbn': '123456789',
            'publication_date': '1949-06-08T00:00:00'
        }
        book_response = self.client.post('/books', json=self.book_data)
        self.book_id = json.loads(book_response.data).get('id')  
        print(f"Created book with ID: {self.book_id}")

        # Creating some initial members
        self.member_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'membership_date': '2024-12-09T00:00:00'
        }
        member_response = self.client.post('/members', json=self.member_data)
        self.member_id = json.loads(member_response.data).get('id') 
        print(f"Created member with ID: {self.member_id}")

    # Test CRUD operations for books
    def test_create_book(self):
        response = self.client.post('/books', json={
            'title': 'Brave New World',
            'author': 'Aldous Huxley',
            'isbn': '987654321',
            'publication_date': '1932-08-18T00:00:00'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Book created successfully', str(response.data))

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn('1984', str(response.data))  

    def test_get_book(self):
       
        response = self.client.get(f'/books/{self.book_id}')
        print(f"Fetching book with ID: {self.book_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1984', str(response.data))  

    def test_update_book(self):
        
        response = self.client.put(f'/books/{self.book_id}', json={
            'title': 'Nineteen Eighty-Four',
            'author': 'George Orwell',
            'isbn': '123456789',
            'publication_date': '1949-06-08T00:00:00'
        })
        print(f"Updating book with ID: {self.book_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Book updated successfully', str(response.data))

    def test_delete_book(self):
        
        response = self.client.delete(f'/books/{self.book_id}')
        print(f"Deleting book with ID: {self.book_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Book deleted successfully', str(response.data))

    # Test CRUD operations for members
    def test_create_member(self):
        response = self.client.post('/members', json={
            'name': 'Jane Doe',
            'email': 'janedoe@example.com',
            'membership_date': '2024-12-09T00:00:00'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Member created successfully', str(response.data))

    def test_get_members(self):
        response = self.client.get('/members')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))  

    def test_get_member(self):
        
        response = self.client.get(f'/members/{self.member_id}')
        print(f"Fetching member with ID: {self.member_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))  

    def test_update_member(self):
        
        response = self.client.put(f'/members/{self.member_id}', json={
            'name': 'Johnathan Doe',
            'email': 'johnathan@example.com',
            'membership_date': '2024-12-09T00:00:00'
        })
        print(f"Updating member with ID: {self.member_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Member updated successfully', str(response.data))

    def test_delete_member(self):
        
        response = self.client.delete(f'/members/{self.member_id}')
        print(f"Deleting member with ID: {self.member_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Member deleted successfully', str(response.data))

    # Test search functionality for books
    def test_search_books_by_title(self):
        response = self.client.get(f'/books/search?title=1984')
        print(f"Searching for book by title '1984'")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1984', str(response.data))

    def test_search_books_by_author(self):
        response = self.client.get(f'/books/search?author=George Orwell')
        print(f"Searching for book by author 'George Orwell'")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1984', str(response.data))


    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
