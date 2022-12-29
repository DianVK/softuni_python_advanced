from collections import deque

substring = deque(input().split())

colors = {
    "all colors": ("red", "yellow", "blue", "orange", "purple", "green"),
    "required colors": {
        "orange": ("red", "yellow"),
        "purple": ("red", "blue"),
        "green": ("yellow", "blue")
    }
}

result = []

while substring:
    last_part = ""
    if len(substring) > 1:
        last_part = substring.pop()
    first_part = substring.popleft()
    for color in (first_part + last_part, last_part + first_part):
        if color in colors["all colors"]:
            result.append(color)
            break
    else:
        for item in (first_part[:-1], last_part[:-1]):
            if item:
                substring.insert(len(substring) // 2, item)

for color, req_colors in colors["required colors"].items():
    if any(x not in result and color in result for x in req_colors):
        result.remove(color)

print(result)

# from collections import deque
# text = deque(input().split())
# main_colors = ["red", "yellow", "blue"]
# secondary_colors = ["orange", "purple", "green"]
# found_colors = []
# while text:
#     first_str = text.popleft()
#     if text:
#         last_str = text.pop()
#     else:
#         last_str = first_str
#     check_text = first_str + last_str
#     if check_text in main_colors or check_text in secondary_colors:
#         if check_text in main_colors:
#             print(check_text)
#             found_colors.append(check_text)
#         if check_text in secondary_colors:
#             print(check_text)
#             found_colors.append(check_text)
#     else:
#         len_first_str = len(first_str)
#         first_str = first_str[0:len_first_str - 1]
#         len_last_str = len(last_str)
#         last_str = last_str[0:len_last_str - 1]
#         text_division = len(text) // 2
#         text = list(text)
#         text = text[0:text_division] + first_str + last_str + text[text_division::]
#         text = deque(text)
