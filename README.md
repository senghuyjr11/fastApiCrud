# FastAPI Book List App

This is a FastAPI application for managing a list of books, demonstrating basic CRUD (Create, Read, Update, Delete) operations with Bootstrap 5 styling. The project uses SQLite as the database to store book information.

## Features
- List all books in a table format.
- Add new books using a form on a separate page.
- Edit and update existing books.
- Delete books with a confirmation alert.
- Styled with Bootstrap 5 for a responsive and clean UI.

## Requirements
- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- Jinja2 (for HTML templating)

## Database
This project uses **SQLite** as the default database, which is set up automatically when you run the application. SQLite is a lightweight, file-based database that's suitable for development and testing environments. By default, a file named `books.db` is created in your project directory to store data.

## Installation
1. **Clone the repository**:  
   `git clone https://github.com/yourusername/fastapi-book-list-app.git`  
   `cd fastApiCrud`

2. **Set up a virtual environment and activate it**:  
   `python -m venv .venv`  
   `source .venv/bin/activate`  *(On Windows use `.venv\Scripts\activate`)*

3. **Install the dependencies**:  
   `pip install fastapi uvicorn sqlalchemy jinja2`

4. **Run the application**:
   `uvicorn main:app --reload`

5. **Access the app**: Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
- **View Books**: The homepage displays a list of all books in a table.
- **Add a Book**: Click the "Add Book" button to go to a form page and add a new book.
- **Edit a Book**: Click the "Edit" button next to a book to modify its details.
- **Delete a Book**: Click the "Delete" button next to a book and confirm the deletion in the popup alert.

## Project Structure
- `main.py`: The main FastAPI application file that defines routes and initializes the app.
- `database.py`: Handles database setup and session creation using SQLAlchemy.
- `models.py`: Contains the `Book` model, which defines the structure of the database table in SQLite.
- `schemas.py`: Defines Pydantic schemas for data validation.
- `templates/`: Contains HTML templates.
  - `base.html`: The base template with Bootstrap styling.
  - `book_list.html`: Displays the list of books and an "Add Book" button.
  - `book_form.html`: Used for adding and editing books.
- `books.db`: The SQLite database file where all data is stored (generated after running the app).

## License
https://senghuyjr11.surge.sh