from .user import User

class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available = {} # {author: [book1, book2, ...]}
        self.rented_books = {} # {username: {book_name: days_to_return}}

    def get_book(self, author: str, tittle: str, rental_days: int, user: User):
        if tittle in self.books_available[author]:
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            rented_by_user = self.rented_books[user.username]
            rented_by_user[tittle] = rental_days
            self.rented_books[user.username] = rented_by_user
            self.books_available[author].remove(tittle)
            user.books.append(tittle)
            return f"{tittle} successfully rented for the next {rental_days} days!"
        return (
            f'The book "{tittle}" is already rented and will be available in '
            f'{self.rented_books[user.username][tittle]} days!'
        )

    def return_book(self, author:str, tittle:str, user: User):
        if tittle not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"
        self.books_available[author].append(tittle)
        del self.rented_books[user.username][tittle]
        user.books.remove(tittle)
