def multiply(times):

    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return result * times
        return wrapper

    return decorator
