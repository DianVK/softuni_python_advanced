def genrange(start: int, end: int):
    for num in range(start, end + 1):
        yield num


print(list(genrange(1, 10)))

# class genrange:
#     def __init__(self,start:int,end:int):
#         self.start = start - 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         self.start += 1
#         return self.start

# def genrange(start: int, end: int):
#     end += 1
#     while end > start:
#         yield start
#         start += 1
