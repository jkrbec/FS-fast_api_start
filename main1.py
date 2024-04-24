from fastapi import FastAPI, HTTPException
from models import Book, Author
from typing import List
from data import authors, books

app = FastAPI()

@app.get("/authors/", response_model=List[Author])
async def list_authors():
    return list(authors.values())

@app.get("/authors/{author_id}", response_model=Author)
async def read_author(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    return authors[author_id]

@app.post("/authors/", response_model=Author)
async def create_author(author: Author):
    if author.id in authors:
        raise HTTPException(status_code=400, detail="Author already exists")
    authors[author.id] = author
    return author

@app.put("/authors/{author_id}", response_model=Author)
async def update_author(author_id: int, author: Author):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    authors[author_id] = author
    return author

@app.delete("/authors/{author_id}", response_model=dict)
async def delete_author(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    del authors[author_id]
    return {"detail": "Author deleted"}

# Books CRUD
@app.get("/books/", response_model=List[Book])
async def list_books():
    return list(books.values())

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=400, detail="Book already exists")
    if book.author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    books[book.id] = book
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    books[book_id] = book
    return book

@app.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"detail": "Book deleted"}



