class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.current_letter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration

        if self.current_letter == len(self.sequence):
            self.current_letter = 0

        self.counter += 1
        current_letter = self.sequence[self.current_letter]
        self.current_letter += 1
        return current_letter



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("\n".strip())

result = sequence_repeat('I Love Python', 16)
for item in result:
    print(item, end ='')


# class sequence_repeat:
#
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == self.number - 1:
#             raise StopIteration
#         self.index += 1
#         return self.sequence[self.index % len(self.sequence)]
