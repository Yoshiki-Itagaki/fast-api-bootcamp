from fastapi  import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'history'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'math'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'geography'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'art'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
