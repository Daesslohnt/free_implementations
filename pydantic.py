"""
It is the alternative to build in dataclasses
"""

import json
from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):

    title: str
    author: str
    publisher: str
    price: int
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

def main() -> None:

    with open("exp_data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].title)

if __name__ == "__main__":
    main()