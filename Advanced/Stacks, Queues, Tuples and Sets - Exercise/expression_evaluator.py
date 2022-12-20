from collections import deque

string_expression = input().split()

numbers = deque()
operators = {
    "+": lambda f, s: f + s,
    "-": lambda f, s: f - s,
    "*": lambda f, s: f * s,
    "/": lambda f, s: f // s
}


for element in string_expression:
    if element in "+-*/":
        while len(numbers) > 1:
            numbers.appendleft(operators[element](numbers.popleft(), numbers.popleft()))
    else:
        numbers.append(int(element))

print(numbers.popleft())



#
# from collections import deque
#
# string_expression = input().split()
#
# numbers = deque()
#
# for element in string_expression:
#     if element in "+-*/":
#         while len(numbers) > 1:
#             num_one = numbers.popleft()
#             num_two = numbers.popleft()
#
#             result = 0
#
#             if element == "+":
#                 result = num_one + num_two
#             elif element == "-":
#                 result = num_one - num_two
#             elif element == "*":
#                 result = num_one * num_two
#             else:
#                 result = num_one // num_two
#
#             numbers.appendleft(result)
#
#     else:
#         numbers.append(int(element))
#
# print(numbers.popleft())