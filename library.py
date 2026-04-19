app_name = "library"
version = "0.1"
is_active = True
book_count = 0
# library = []

print(f"Library app {app_name} version {version} is active: {is_active}")


def create_book(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    is_read: bool | None = None,
    genre: str | None = None,
):
    # global book_count
    # book_count += 1
    # print(f"Book created: '{title} by {author}. Total books: {book_count}")
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


def book_era(book: dict) -> bool | str:
    if book["year"] and book["year"] > 2000:
        return "new"
    return True


def add_book(library: list, book: dict) -> None:
    # global library
    library.append(book)
    print(f"{book['title']}    {len(library)}")


def remove_book(library: list, title: str) -> None:
    # check library list, remove the book with {title}
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


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_books(self, book) -> None:
        self.books.append(book)


def main():
    book1 = create_book(title="Karamazov brothers", author="Dostoyevski", year=1880)
    print(is_classic(book1))
    library = []
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


if __name__ == "__main__":
    main()
