import json
from typing import Union, Callable, Any, List, Dict


class CustomException(Exception):
    """
    Custom Exception class for handling library-specific errors.
    """

    pass


def create_book(
    title: Union[str, None] = None,
    author: Union[str, None] = None,
    year: Union[int, None] = None,
    is_read: Union[bool, None] = None,
    genre: Union[str, None] = None,
) -> Dict[str, Any]:
    """
    Returns:
        A dictionary containing the book data with keys matching the parameters.

    Parameters (all of them are optional):
        title, author, year, is_read, genre.
    """
    book = {
        "title": title,
        "author": author,
        "year": year,
        "is_read": is_read,
        "genre": genre,
    }
    return book


def is_classic(book: Dict[str, Any]) -> bool:
    """
    Returns:
        True if the book was published before 1950, False otherwise.

    Parameters:
        book: A dictionary containing book data including a 'year' key.
    """
    if book["year"] and book["year"] < 1950:
        return True
    return False


def book_era(book: Dict[str, Any]) -> str:
    """
    Returns:
        `new` if published after 2000, 'old' otherwise.

    Parameter:
        book: A dictionary containing book data including a 'year' key.
    """
    if book["year"] and book["year"] > 2000:
        return "new"
    return "old"


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
        print(f"function {func.__name__} was called {countt} times")
        return func(*args, **kwargs)

    return inner


@count_call
def add_book(library: Union[List[Any], None], book: Dict[str, Any]) -> None:
    """
    Add a book to the library collection.
    This function is decorated with @count_call to track how many times it's called.

    Parameters:
        library: The library list to add the book to (must not be None).
        book: The book dictionary to add to the library.

    Raises:
        AssertionError: If library is None (with CustomException).
    """
    assert library is not None, CustomException("You should have a library first!")
    library.append(book)
    print(
        f"{book['title']} is added to library. Currently there are {len(library)} books"
    )


def remove_book(library: Union[List[Any], None], title: str) -> None:
    """
    Remove a book from the library by its title.

    Parameters:
        library: The library list to remove the book from (must not be None).
        title: The title of the book to remove.

    Raises:
        AssertionError: If library is None (with CustomException).
    """
    assert library is not None, CustomException("No library!")
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print(f"Book with title {title} is removed")
            return
    print(f"Book with title {title} not found")


def all_genres(library: Union[List[Any], None]) -> None:
    """
    Display all unique genres present in the library.

    Parameters:
        library: The library list to analyze (must not be None).

    Raises:
        AssertionError: If library is None (with CustomException).
    """
    genres = set()
    assert library is not None, CustomException("No library!")
    for elem in library:
        genres.add(elem["genre"])
    print(genres)


def book_iterator(
    library: Union[List[Any], None], genre_filter: Union[str, None] = None
):
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
    assert library is not None, CustomException("You should have a library first!")
    for book in library:
        if genre_filter is None or book.get("genre") == genre_filter:
            yield book


def write_to_json(data: object, filename="library.json") -> None:
    """
    Write data to a JSON file.

    Parameters:
        data: The Python object to be serialized to JSON.
        filename: The name of the file to write to (default: "library.json").

    Raises:
        AssertionError: If data is None (with CustomException).
    """
    assert data is not None, CustomException("Specify the data to write to json")
    try:
        with open(file=filename, mode="w", encoding="utf-8") as f:
            json.dump(obj=data, fp=f, indent=4, ensure_ascii=False)
    except (IOError, OSError, TypeError) as e:
        print(f"Error writing to {filename}: {e}")


def read_from_json(filename="library.json") -> Any:
    """
    Read and parse JSON data from a file.

    Parameters:
        filename: The name of the file to read from (default: "library.json").

    Returns:
        The deserialized Python object from the JSON file.

    Raises:
        CustomException: If file not found, JSON is malformed, or IO errors occur.
    """
    try:
        with open(file=filename, mode="r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise CustomException(f"No file named {filename}")
    except json.JSONDecodeError as e:
        raise CustomException(f"Error decoding JSON from {filename}: {e}")
    except (IOError, OSError):
        raise CustomException("This seems like a serious issue. Call Jeff Bezos.")
    else:
        print("else block")
    finally:
        print("life goes on")


def save_library(library: Union[List[Any], None], filename="library.json") -> None:
    """
    Save the entire library collection to a JSON file.

    Parameters:
        library: The library list to save (must not be None).
        filename: The name of the file to save to (default: "library.json").

    Raises:
        CustomException: If library is None.
    """
    library_data: List[object] = []
    if library is None:
        raise CustomException("You should have a library first!")
    if library:
        for book in library:
            if isinstance(book, dict):
                library_data.append(
                    {
                        "title": book.get("title"),
                        "author": book.get("author"),
                        "year": book.get("year"),
                        "genre": book.get("genre"),
                        "is_read": book.get("is_read"),
                    }
                )
            else:
                library_data.append(
                    {
                        "title": book.title,
                        "author": book.author,
                        "year": book.year,
                        "genre": book.genre,
                        "is_read": book.is_read,
                    }
                )
        write_to_json(library_data, filename)


class Book:
    """
    Base class representing books.
    """

    def __init__(
        self,
        title: Union[str, None],
        author: Union[str, None],
        year: Union[int, str, None],
        genre: Union[str, None],
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_read = False

    def mark_as_read(self) -> None:
        self.is_read = True
        print(f"Book '{self.title} marked as read'")

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

    # I could have made this method specifically type hinted to class Book.
    # But I am keeping it this way for now, maybe I will change it later, if needed.
    def add_books(self, book: Book) -> None:
        self.books.append(book)

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
        title: Union[str, None],
        author: Union[str, None],
        year: Union[str, int, None],
        genre: Union[str, None],
        filename: Union[str, None],
    ):
        super().__init__(title, author, year, genre)
        self.filename = filename


def main():
    """
    Main functionality.
    """
    app_name = "library"
    version = "0.1"
    is_active = True
    library = []
    print(
        f"{app_name} {'is active' if is_active else 'is not active'} with version {version}"
    )
    book1 = create_book(title="Karamazov brothers", author="Dostoyevski", year=1880)
    print(f"book {book1.get('title')} is classic: {is_classic(book1)}")

    add_book(
        library,
        create_book(title="Ali Nino", author="Qurban Seid", year=1937, genre="Roman"),
    )
    add_book(
        library,
        create_book(title="1984", author="George Orwell", year=1949, genre="Distopia"),
    )
    add_book(
        library,
        create_book(
            title="Sapiens", author="Yuval Noah Harari", year=2011, genre="Tarix"
        ),
    )

    classic_books = [elem["title"] for elem in library if is_classic(elem)]
    print(classic_books)

    authors = [elem["author"] for elem in library]
    print(authors)

    year_2000 = [elem["year"] for elem in library]
    print(year_2000)

    all_genres(library)

    write_to_json(book1, "book1.json")

    print("\nBooks with genre 'Roman':")
    for book in book_iterator(library, genre_filter="Roman"):
        print(book["title"])

    ebook1 = EBook("26-lar", "Semed Vurgun", 1998, "poem", "Bakinin_derdi_var.epub")
    print(f"\nEBook created: {ebook1.title}, filename: {ebook1.filename}")
    print("Let's call it!")
    print(ebook1)

    save_library(library, "my_library.json")
    loaded_library = read_from_json("my_library.json")
    if loaded_library:
        print(f"\nLoaded {len(loaded_library)} books from JSON")

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
