def reverse_text(text):
    text = text[::-1]
    for x in range(len(text)):
        current_letter = text[x]
        yield current_letter


for char in reverse_text("step"):
    print(char, end='')


# def reverse_text(text: str):
#     index = len(text) - 1
#     while index >= 0:
#         yield text[index]
#         index -= 1

