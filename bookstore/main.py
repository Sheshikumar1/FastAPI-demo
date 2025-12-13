from fastapi import FastAPI,HTTPException
from starlette.responses import JSONResponse
from models import Book
from pydantic import BaseModel
app=FastAPI()

@app.get("/book/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id":book_id,
        "title":"the great india",
        "author":"sheshi"
    }

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        'author_id':author_id,
        'name':"sheshi"
    }

@app.get("/books")
async def read_books(year: int=None):
    if year:
        return {
            'year':year,
            'books':['Book 1','Book 2']
        }
    return {'books':["ALL Books"]}

@app.post("/book")
async def create_book(book: Book):
    return book

class BooKResponse(BaseModel):
    title:str
    author:str
@app.get("/allbooks")
async def read_all_books() ->list[BooKResponse]:
    return [
        {
            "id":1,
            "title":"1984",
            "auther":"George Orwell"
        },
        {
            "id":1,
            "title":"The great Gatesby",
            "author":"F. Scott Fitzgerald"
        },
    ]

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message":"Oops! Something went wrong "
        },
    )

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)