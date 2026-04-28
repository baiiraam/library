import json
from typing import Callable, Any, List, Optional


class CustomException(Exception):
    """
    Custom Exception class for handling library-specific errors.
    """

    pass


def count_call(func: Callable) -> Callable:
    """
    Decorator that counts how many times a function is called.

    Parameters:
        func: The function to be decorated.

    Returns:
        A wrapper function that tracks call count and then calls the original function.
    """
    countt = 0

    def inner(*args, **kwargs):
        nonlocal countt
        countt += 1
        func_name = getattr(func, "__name__")
        print(f"function {func_name} was called {countt} times")
        return func(*args, **kwargs)

    return inner


class Book:
    """
    Base class representing books.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
        genre: Optional[str] = None,
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_read = False

    def is_classic(self) -> bool:
        if self.year and self.year < 1950:
            return True
        return False

    def book_era(self) -> str:
        if self.year and self.year < 2000:
            return "old"
        return "new"

    def mark_as_read(self) -> None:
        self.is_read = True
        print(f"Book {self.title} marked as read'")

    def display_info(self) -> None:
        if self.is_read:
            print(f"Book {self.title} is read")
        else:
            print(f"Book {self.title} is not read")

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}"

    def __repr__(self) -> str:
        return f"Class: {self.__class__}"


class Library:
    """
    Library class.
    """

    def __init__(self) -> None:
        self.books: List[Book] = []

    @count_call
    def add_books(self, book: Book) -> None:
        if not self.validator(book):
            raise CustomException("Only Book type allowed")
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        if not isinstance(title, str):
            raise CustomException("Title must be string")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

    @staticmethod
    def validator(something: Any) -> bool:
        return isinstance(something, Book)

    def book_iterator(self):
        for book in self.books:
            yield book

    def all_genres(self) -> set:
        genres = set()
        if not len(self.books) > 0:
            raise CustomException("no books in library")
        for book in self.books:
            genres.add(book.genre)
        return genres

    def __str__(self) -> str:
        return f"Library has {len(self.books)} books"

    def __repr__(self) -> str:
        return f"{self.__class__}"


class EBook(Book):
    """
    Child class of Book.
    """

    def __init__(
        self,
        title: Optional[str],
        author: Optional[str],
        year: Optional[int],
        genre: Optional[str],
        filename: Optional[str],
    ):
        super().__init__(title, author, year, genre)
        self.filename = filename


class JsonWriter:
    filename = "my_library.json"

    def __init__(self):
        pass

    @staticmethod
    def validate_book(something: Book) -> bool:
        return isinstance(something, Book)

    @staticmethod
    def validate_library(something: Library) -> bool:
        return isinstance(something, Library)

    def write_book(self, other: Book):
        if not self.validate_book(other):
            raise CustomException("object should be of Book class")
        book_dict = {
            "author": other.author,
            "genre": other.genre,
            "title": other.title,
            "year": other.year,
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(obj=book_dict, fp=f, indent=2)

    def write_library(self, other: Library):
        if not self.validate_library(other):
            raise CustomException("Only Library type allowed")
        books = []
        for book in other.books:
            book_dict = {
                "author": book.author,
                "title": book.title,
                "genre": book.genre,
                "year": book.year,
            }
            books.append(book_dict)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=2)


class JsonReader:
    filename = "my_library.json"

    @staticmethod
    def read_file(filename):
        with open(file=filename, mode="r", encoding="utf-8") as f:
            return json.load(f)


def main():
    """
    Main functionality.
    """
    app_name = "library"
    version = "0.1"
    is_active = True
    library = Library()
    print(
        f"{app_name} {'is active' if is_active else 'is not active'} with version {version}"
    )
    book1 = Book(title="Karamazov brothers", author="Dostoyevski", year=1880)
    print(f"book {book1.title} is classic: {book1.is_classic()}")

    book2 = Book(title="Ali Nino", author="Qurban Seid", year=1937, genre="Roman")
    book3 = Book(title="1984", author="George Orwell", year=1949, genre="Distopia")
    book4 = Book(title="Sapiens", author="Yuval Noah Harari", year=2011, genre="Tarix")

    library.add_books(book1)
    library.add_books(book2)
    library.add_books(book3)
    library.add_books(book4)

    classic_books = [book.title for book in library.books if book.is_classic()]
    print(classic_books)

    authors = [book.author for book in library.books]
    print(authors)

    year_2000 = [book.year for book in library.books]
    print(year_2000)

    jsonwriter = JsonWriter()
    jsonwriter.write_book(book1)

    print(library.all_genres())

    ebook1 = EBook("26-lar", "Semed Vurgun", 1998, "poem", "Bakinin_derdi_var.epub")
    print(f"\nEBook created: {ebook1.title}, filename: {ebook1.filename}")
    print("Let's call it!")
    print(ebook1)

    jsonwriter.write_library(library)

    jsonreader = JsonReader()
    books = jsonreader.read_file("my_library.json")

    if books:
        print(f"\nLoaded {len(books)} books from JSON")

    book_1 = Book(
        title="Harry Potter and the Sorcerer's Stone",
        author="J.K.Rowling",
        year=1997,
        genre="fantasy",
    )
    book_2 = Book(
        title="Harry Potter and the Chamber of Secrets",
        author="J.K.Rowling",
        year=1998,
        genre="fantasy",
    )
    book_3 = EBook(
        title="Harry Potter and the Prisoner of Azkaban",
        author="J.K.Rowling",
        year=1999,
        genre="fantasy",
        filename="Azkaban_scenario.txt",
    )

    library_1 = Library()
    library_1.add_books(book_1)
    library_1.add_books(book_2)
    library_1.add_books(book_3)

    for book in library_1.books:
        book.mark_as_read()
    for book in library_1.books:
        book.display_info()


# Entrypoint
if __name__ == "__main__":
    main()
