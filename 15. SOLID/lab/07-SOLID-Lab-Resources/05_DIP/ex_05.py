class Book:
    def __init__(self, content: str):
        self.content = content

class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class PaperFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:2]

class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book

f = Formatter()
pf = PaperFormatter()

b = Book("Hello world!")
printer = Printer()
print(printer.get_book(b, f))
print(printer.get_book(b, pf))