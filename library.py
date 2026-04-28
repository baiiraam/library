import json
from typing import Callable, Any, List, Optional


class CustomException(Exception):
    """
    Custom Exception class for handling library-specific errors.
    """

    pass


# def create_book(
#     title: Optional[str] = None,
#     author: Optional[str] = None,
#     year: Optional[int] = None,
#     is_read: Optional[bool] = None,
#     genre: Optional[str] = None,
# ) -> Dict[str, Any]:
#     """
#     Returns:
#         A dictionary containing the book data with keys matching the parameters.

#     Parameters (all of them are optional):
#         title, author, year, is_read, genre.
#     """
#     book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "is_read": is_read,
#         "genre": genre,
#     }
#     return book


# def is_classic(book: Dict[str, Any]) -> bool:
#     """
#     Returns:
#         True if the book was published before 1950, False otherwise.

#     Parameters:
#         book: A dictionary containing book data including a 'year' key.
#     """
#     if book["year"] and book["year"] < 1950:
#         return True
#     return False


# def book_era(book: Dict[str, Any]) -> str:
#     """
#     Returns:
#         `new` if published after 2000, 'old' otherwise.

#     Parameter:
#         book: A dictionary containing book data including a 'year' key.
#     """
#     if book["year"] and book["year"] > 2000:
#         return "new"
#     return "old"


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

    # @count_call
    # def add_book(library: Optional[List[Any]], book: Dict[str, Any]) -> None:
    #     """
    #     Add a book to the library collection.
    #     This function is decorated with @count_call to track how many times it's called.

    #     Parameters:
    #         library: The library list to add the book to (must not be None).
    #         book: The book dictionary to add to the library.

    #     Raises:
    #         AssertionError: If library is None (with CustomException).
    #     """
    #     assert library is not None, CustomException("You should have a library first!")
    #     library.append(book)
    #     print(
    #         f"{book['title']} is added to library. Currently there are {len(library)} books"
    #     )

    # def remove_book(library: Optional[List[Any]], title: str) -> None:
    # """
    # Remove a book from the library by its title.

    # Parameters:
    #     library: The library list to remove the book from (must not be None).
    #     title: The title of the book to remove.

    # Raises:
    #     AssertionError: If library is None (with CustomException).
    # """
    # assert library is not None, CustomException("No library!")
    # for book in library:
    #     if book["title"] == title:
    #         library.remove(book)
    #         print(f"Book with title {title} is removed")
    #         return
    # print(f"Book with title {title} not found")

    # def all_genres(library: Optional[List[Any]]) -> None:
    #     """
    #     Display all unique genres present in the library.

    #     Parameters:
    #         library: The library list to analyze (must not be None).

    #     Raises:
    #         AssertionError: If library is None (with CustomException).
    #     """
    #     genres = set()
    #     assert library is not None, CustomException("No library!")
    #     for elem in library:
    #         genres.add(elem["genre"])
    #     print(genres)

    # def book_iterator(
    #     library: Optional[List[Any]], genre_filter: Optional[str] = None
    # ):
    """
    Generator function that yields books from the library, optionally filtered by genre.

    Parameters:
        library: The library list to iterate over (must not be None).
        genre_filter: Optional genre to filter books by. If None, all books are yielded.

    Yields:
        Book dictionaries one at a time from the library.

    Raises:
        AssertionError: If library is None (with CustomException).
    """
    # assert library is not None, CustomException("You should have a library first!")
    # for book in library:
    #     if genre_filter is None or book.get("genre") == genre_filter:
    #         yield book


# def write_to_json(data: object, filename="library.json") -> None:
#     """
#     Write data to a JSON file.

#     Parameters:
#         data: The Python object to be serialized to JSON.
#         filename: The name of the file to write to (default: "library.json").

#     Raises:
#         AssertionError: If data is None (with CustomException).
#     """
#     assert data is not None, CustomException("Specify the data to write to json")
#     try:
#         with open(file=filename, mode="w", encoding="utf-8") as f:
#             json.dump(obj=data, fp=f, indent=4, ensure_ascii=False)
#     except (IOError, OSError, TypeError) as e:
#         print(f"Error writing to {filename}: {e}")


# def read_from_json(filename="library.json") -> Any:
#     """
#     Read and parse JSON data from a file.

#     Parameters:
#         filename: The name of the file to read from (default: "library.json").

#     Returns:
#         The deserialized Python object from the JSON file.

#     Raises:
#         CustomException: If file not found, JSON is malformed, or IO errors occur.
#     """
#     try:
#         with open(file=filename, mode="r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         raise CustomException(f"No file named {filename}")
#     except json.JSONDecodeError as e:
#         raise CustomException(f"Error decoding JSON from {filename}: {e}")
#     except (IOError, OSError):
#         raise CustomException("This seems like a serious issue. Call Jeff Bezos.")
#     else:
#         print("else block")
#     finally:
#         print("life goes on")


# def save_library(library: Optional[List[Any]], filename="library.json") -> None:
#     """
#     Save the entire library collection to a JSON file.

#     Parameters:
#         library: The library list to save (must not be None).
#         filename: The name of the file to save to (default: "library.json").

#     Raises:
#         CustomException: If library is None.
#     """
#     library_data: List[object] = []
#     if library is None:
#         raise CustomException("You should have a library first!")
#     if library:
#         for book in library:
#             if isinstance(book, dict):
#                 library_data.append(
#                     {
#                         "title": book.get("title"),
#                         "author": book.get("author"),
#                         "year": book.get("year"),
#                         "genre": book.get("genre"),
#                         "is_read": book.get("is_read"),
#                     }
#                 )
#             else:
#                 library_data.append(
#                     {
#                         "title": book.title,
#                         "author": book.author,
#                         "year": book.year,
#                         "genre": book.genre,
#                         "is_read": book.is_read,
#                     }
#                 )
#         write_to_json(library_data, filename)


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
        assert self.validator(book), CustomException("oops")
        self.books.append(book)

    def remove_book(self, title) -> Optional[str]:
        assert isinstance(title, str), CustomException("oops")
        for book in self.books:
            if book.title == "title":
                self.books.remove(book)
                return
        return "book not found"

    @staticmethod
    def validator(something: Any) -> bool:
        return isinstance(something, Book)

    def book_iterator(self):
        for book in self.books:
            yield book

    def all_genres(self) -> set:
        genres = set()
        assert len(self.books) > 0, "no books in library"
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
    def validate_book(something):
        return isinstance(something, Book)

    @staticmethod
    def validate_library(something):
        return isinstance(something, Library)

    def write_book(self, other):
        assert self.validate_book(other), CustomException(
            "object should be of Book class"
        )
        book_dict = {
            "author": other.author,
            "genre": other.genre,
            "title": other.title,
            "year": other.year,
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(obj=book_dict, fp=f, indent=2)

    def write_library(self, other):
        assert self.validate_library(other), CustomException("oops")
        for book in other.books:
            self.write_book(book)


class JsonReader:
    filename = "my_library.json"

    @staticmethod
    def read_file(filename):
        with open(file=filename, mode="r", encoding="utf-8") as f:
            contents = f.read()
        return contents


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

    library.all_genres()

    jsonwriter = JsonWriter()
    jsonwriter.write_book(book1)

    library.all_genres()

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
