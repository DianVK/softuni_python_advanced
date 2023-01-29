from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for pos, show in enumerate(library.user_records):
            if show.user_id == user_id:
                if show.username != new_username:
                    if show.username in library.rented_books:
                        library.rented_books = library.rented_books.pop(show.username)
                    show.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return "Please check again the provided username - it should be different than the username used so far!"
            return f"There is no user with id = {user_id}!"
