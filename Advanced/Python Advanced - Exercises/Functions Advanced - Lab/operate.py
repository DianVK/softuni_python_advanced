def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for x in args[1:]:
            result -= x
    elif operator == "/":
        for x in args[1:]:
            result /= x
    elif operator == "*":
        for x in args[1:]:
            result *= x
    return result

# def operate(operator,*args):
#     global result
#     if operator == "+":
#         result = 0
#         for el in args:
#             result += el
#     elif operator == "-":
#         result = 0
#         for el in args:
#             result -= el
#     elif operator == "*":
#         result = 1
#         for el in args:
#             result *= el
#     elif operator == "/":
#         result = 1
#         for el in args:
#             result /= el
#     return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))