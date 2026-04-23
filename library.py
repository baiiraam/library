import json
from typing import Union


def create_book(
    title: Union[str, None] = None,
    author: Union[str, None] = None,
    year: Union[int, None] = None,
    is_read: Union[bool, None] = None,
    genre: Union[str, None] = None,
):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "is_read": is_read,
        "genre": genre,
    }
    return book


def is_classic(book: dict) -> bool:
    if book["year"] and book["year"] < 1950:
        return True
    return False


def book_era(book: dict) -> Union[bool, str]:
    if book["year"] and book["year"] > 2000:
        return "new"
    return True


def count_call(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    wrapper.counter = 0
    return wrapper


@count_call
def add_book(library: list, book: dict) -> None:
    library.append(book)
    print(
        f"{book['title']} is added to library. Currently there are {len(library)} books"
    )


def remove_book(library: list, title: str) -> None:
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print(f"Book with title {title} is removed")
            return
    print(f"Book with title {title} not found")


def all_genres(library: list) -> None:
    genres = set()
    for elem in library:
        genres.add(elem["genre"])
    print(genres)


def book_iterator(library, genre_filter=None):
    for book in library:
        if genre_filter is None or book.get("genre") == genre_filter:
            yield book


def write_to_json(data, filename="library.json") -> None:
    try:
        with open(file=filename, mode="w", encoding="utf-8") as f:
            json.dump(obj=data, fp=f, indent=4, ensure_ascii=False)
    except (IOError, OSError, TypeError) as e:
        print(f"Error writing to {filename}: {e}")


def read_from_json(filename="library.json") -> None:
    try:
        with open(file=filename, mode="r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filename}: {e}")
        return None
    except (IOError, OSError) as e:
        print(f"Error reading {filename}: {e}")
        return None


def save_library(library, filename="library.json"):
    library_data = []
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
    def __init__(self, title, author, year, genre) -> None:
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
        if self.title == "26-lar":
            try:
                with open(file="text.txt", mode="r", encoding="utf-8") as f:
                    filecontents = f.readline()
                    return filecontents
            except FileNotFoundError:
                return f"Title {self.title}, Author: {self.author}"
        else:
            return f"Title: {self.title}, Author: {self.author}"

    def __repr__(self) -> str:
        return f"Class: {self.__class__}"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_books(self, book) -> None:
        self.books.append(book)

    def __str__(self) -> str:
        return f"Library has {len(self.books)} books"

    def __repr__(self) -> str:
        return f"{self.__class__}"


class EBook(Book):
    def __init__(self, title, author, year, genre, filename):
        super().__init__(title, author, year, genre)
        self.filename = filename


def main():
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

    print(f"\nadd_book was called {add_book.counter} times")

    ebook1 = EBook("26-lar", "Semed Vurgun", 1998, "poem", "Bakinin_derdi_var.epub")
    print(f"\nEBook created: {ebook1.title}, filename: {ebook1.filename}")
    print("Let's call it!")
    print(ebook1)

    save_library(library, "my_library.json")
    loaded_library = read_from_json("my_library.json")
    if loaded_library:
        print(f"\nLoaded {len(loaded_library)} books from JSON")


if __name__ == "__main__":
    app_name = "library"
    version = "0.1"
    is_active = True
    book_count = 0
    library = []
    print(
        f"{app_name} {'is active' if is_active else 'is not active'} with version {version}"
    )
    main()
