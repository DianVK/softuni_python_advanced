def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

# def tags(type_text):
#     def decorator(func):
#         def wrapper(*args):
#             return f"<{type_text}>{func(''.join(args))}</{type_text}>"
#         return wrapper
#     return decorator
