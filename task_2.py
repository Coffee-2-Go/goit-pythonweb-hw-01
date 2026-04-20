# Module for managing a library of books using the Facade pattern

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import logging


logger = logging.getLogger("LibraryLogger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)


@dataclass
class Book:
    title: str
    author: str
    year: int


class BookStorage(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_by_title(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[Book]:
        pass


class ListBookStorage(BookStorage):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def remove_by_title(self, title: str) -> bool:
        for i, book in enumerate(self._books):
            if book.title.lower() == title.lower():
                del self._books[i]
                return True
        return False

    def get_all(self) -> list[Book]:
        return self._books.copy()


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def list_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self, storage: BookStorage) -> None:
        self.storage = storage

    def add_book(self, book: Book) -> None:
        self.storage.add(book)

    def remove_book(self, title: str) -> bool:
        return self.storage.remove_by_title(title)

    def list_books(self) -> list[Book]:
        return self.storage.get_all()


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> bool:
        if not title or not author:
            return False

        try:
            year_int = int(year)
        except ValueError:
            return False

        self.library.add_book(Book(title, author, year_int))
        return True

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> bool:
        if not self.library.list_books():
            logger.info("Library is empty.")
            return False

        for book in self.library.list_books():
            logger.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )
        return True


def main() -> None:
    library = Library(ListBookStorage())
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
