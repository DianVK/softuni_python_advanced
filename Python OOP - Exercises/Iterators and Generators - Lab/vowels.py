class vowels:
    ALL_VOWELS = "AEIUYOaeiuyo"

    def __init__(self,sequence: str):
        self.sequence = sequence
        self.sorted_vowels = [x for x in self.sequence if x in vowels.ALL_VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if self.sorted_vowels:
            return self.sorted_vowels.pop(0)
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
