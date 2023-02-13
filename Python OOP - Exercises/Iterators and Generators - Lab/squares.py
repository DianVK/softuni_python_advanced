def squares(num: int):
    first_num = 1
    while first_num <= num:
        yield first_num ** 2
        first_num += 1


print(list(squares(5)))

# class squares:
#
#     def __init__(self, n):
#         self.n = n
#         self.number_counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number_counter < self.n:
#             self.number_counter += 1
#             return self.number_counter ** 2
#
#         raise StopIteration

# class squares:
#     def __init__(self, end: int):
#         self.start = 0
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         self.start += 1
#         return self.start ** 2
