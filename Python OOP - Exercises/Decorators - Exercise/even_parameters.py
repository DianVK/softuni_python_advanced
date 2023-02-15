def even_parameters(function):

    def wrapper(*args):
        for x in args:

            if isinstance(x, int) and x % 2 == 0:
                continue

            return f"Please use only even numbers!"
        return function(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))





















# def even_parameters(func):
#     def wrapper(*args):
#         for num in args:
#
#             if isinstance(num, int) and num % 2 == 0:
#                 continue
#             return "Please use only even numbers!"
#
#         return func(*args)
#
#     return wrapper
#
#
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
#
#
# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))
