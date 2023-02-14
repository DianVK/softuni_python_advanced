class countdown_iterator():

    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration

        self.count -= 1
        return self.count + 1


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print("\n".strip())

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")


# class countdown_iterator:
#     def __init__(self, number: int):
#         self.number = number + 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number <= 0:
#             raise StopIteration
#
#         self.number -= 1
#         return self.number
