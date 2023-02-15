def make_bold(func):

    def wrapper(*args):
        return f"<b>{func(*args)}</b>"
    return wrapper


def make_italic(func):

    def wrapper(*args):
        return f"<i>{func(*args)}</i>"
    return wrapper


def make_underline(func):

    def wrapper(*args):
        return f"<u>{func(*args)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

# from functools import wraps
#
#
# def make_bold(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#
#     return wrapper
#
#
# def make_italic(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#
#     return wrapper
#
#
# def make_underline(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<u>{func(*args, **kwargs)}</u>"
#
#     return wrapper
