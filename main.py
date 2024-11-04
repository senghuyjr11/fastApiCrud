from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Book

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create tables
Base.metadata.create_all(bind=engine)

# List Books
@app.get("/")
def read_books(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse("book_list.html", {"request": request, "books": books})

# Create Book
@app.get("/add", response_class=RedirectResponse)
def create_book_form(request: Request):
    return templates.TemplateResponse("book_form.html", {"request": request})

@app.post("/add")
def create_book(title: str = Form(...), author: str = Form(...), year: int = Form(...), description: str = Form(None), db: Session = Depends(get_db)):
    new_book = Book(title=title, author=author, year=year, description=description)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return RedirectResponse(url="/", status_code=303)

# Update Book
@app.get("/edit/{book_id}")
def edit_book(book_id: int, request: Request, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    return templates.TemplateResponse("book_form.html", {"request": request, "book": book})

@app.post("/edit/{book_id}")
def update_book(book_id: int, title: str = Form(...), author: str = Form(...), year: int = Form(...), description: str = Form(None), db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    book.title = title
    book.author = author
    book.year = year
    book.description = description
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Delete Book
@app.post("/delete/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
