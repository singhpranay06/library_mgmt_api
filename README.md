# Library Management System (LMS) API

## Description

This project is a simple **Library Management System (LMS)** built using **Flask**, which supports CRUD operations for **books** and **members**. 

## Features

- **CRUD operations** for managing books and members
- **Search functionality** for books by title or author

## Prerequisites

- Python 3.x
- Flask (install via `pip`)


## How to Run?

Since this project is an API with no front-end or client application, the main way to interact with the project is through the test suite, which validates the API's functionality.

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/singhpranay06/library_mgmt_api.git

2. Navigate to the project directory:
   
   ```bash
   cd library_mgmt_api

3. Run the unit tests to validate the API endpoints:
   
   ```bash
   python -m unittest test_library.py

This will execute the test cases that validate the API routes and functionality, such as:

- POST /books to create a book
- GET /books to retrieve all books
- GET /books/<id> to retrieve a book by ID
- PUT /books/<id> to update a book's details
- DELETE /books/<id> to delete a book
- and similar endpoints for managing library members as well.

## Running the Flask App (Optional)

Run the app:

    ```bash
    python main.py

# Design Choices

- In-memory storage: The application uses lists (books and members) to store the data in memory. This approach was selected because this is a simplified version of the system without a real database connection. This approach suits testing, but a production system would require persistent storage, such as an SQL or NoSQL database.

- Endpoints: Each entity, such as Book and Member, has its own set of endpoints:

  1. GET: Fetch data.
  2. POST: Add new entries.
  3. PUT: Update existing data.
  4. DELETE: Remove data.
  5. Data Validation: Minimal validation is included in this implementation. In a production system, data validation, error handling, and logging should be much more robust.
  6. Testing: Unit tests were written to validate all API endpoints and ensure the proper behavior of each function (CRUD operations for both books and members and search).


# Assumptions:
- **No external database:** The system is using in-memory data storage (i.e., lists) for simplicity. All data is lost when the application stops. In a production system a robust DBMS is required.
- **No UI:** This project focuses solely on the API backend. There is no graphical user interface (UI), and users will interact with the system through API requests (e.g., via Postman or curl).
- **Data types and format:** The API assumes general data types reuired by the entities of a library. There is minimal input validation, so invalid data may lead to unexpected behavior.

# Limitations:
- **In-memory storage:** Since there is no database, the data is not permanent. Upon restarting the server, all books and members will be lost.
- **No authentication:** There is no security layer for user authentication, so anyone with access to the API can interact with it.
- **Limited validation:** Input validation is minimal, and error handling is rudimentary, needs to be enhanced for production environments.
