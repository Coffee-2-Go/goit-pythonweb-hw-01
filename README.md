# Tier 2. Module 6 - Fullstack Web Development with Python

## Topic 1. Homework - Python Development

There will be two homework assignments.

Both assignments require typing. Instead of the `print` statement, you should use `INFO`-level logging. Use `black` for code formatting.

### Task 1. Factory Pattern

#### Technical task

The following code represents a simple system for creating vehicles. We have two classes: `Car` and `Motorcycle`. Each class has a `start_engine()` method that simulates starting the engine of the corresponding vehicle. Currently, to create a new vehicle, we simply create an instance of the corresponding class with the `make` and `model` specified.

```Python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

# Використання
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
```

The next step is to create vehicles with different regional specifications, for example, for the United States `US Spec` and the European Union `EU Spec`.

**Your task** is to implement the factory pattern, which will allow you to create vehicles with different regional specifications without changing the main vehicle classes.

#### Task 1 execution:

1. Create an abstract base class `Vehicle` with a `start_engine()` method.
2. Change the `Car` and `Motorcycle` classes to inherit from `Vehicle`.
3. Create an abstract class `VehicleFactory` with `create_car()` and `create_motorcycle()` methods.
4. Implement two factory classes: `USVehicleFactory` and `EUVehicleFactory`. These factories should create cars and motorcycles with a region tag, for example, `Ford Mustang (US Spec)` for the United States, respectively.
5. Change the source code so that it uses factories to create vehicles.

#### Expected result

- Code that allows you to easily create vehicles for different regions using the appropriate factories.

### Task 2. SOLID

#### Technical task

Here is a simplified program for managing a book library. The program has the ability to add new books, remove books, and display all books in the library. The user can interact with the program via the command line, using the add, remove, show, and exit commands.

```Python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

def main():
    library = Library()

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif command == "show":
            library.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```

**Your task** is to rewrite the code to follow the SOLID principles.

#### Task 2 execution:

1. To implement the Single Responsibility Principle (SRP), create a `Book` class that will be responsible for storing information about the book.
2. To implement the Open/Closed Principle (OCP), make the `Library` class extendable for new functionality without changing its code.
3. To implement the Lisk Substitution Principle (LSP), make sure that any class that inherits the `LibraryInterface` interface can replace the `Library` class without breaking the program.
4. To implement the Separation of Interfaces (ISP), use the `LibraryInterface` interface to explicitly specify the methods that are required to work with the `Library`.
5. To implement the Dependency Inversion Principle (DIP), make higher-level classes, such as LibraryManager, depend on abstractions (interfaces) rather than on concrete class implementations.

```Python
from abc import ABC, abstractmethod

class Book:
    pass

class LibraryInterface(ABC):
    pass

class Library(LibraryInterface):
    pass

class LibraryManager:
    pass

def main():
    library = Library()
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
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```
