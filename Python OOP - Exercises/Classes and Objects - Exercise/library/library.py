from user import User


class Library():
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for name in self.rented_books:
            for book, days_return in self.rented_books[name].items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days_return} days!'

        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].pop(self.books_available[author].index(book_name))
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self,author:str, book_name:str, user: User):
        if book_name in user.books:
            user.books.pop(user.books.index(book_name))
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"