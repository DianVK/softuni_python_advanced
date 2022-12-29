text = input()
all_chars = {}
for char in range(len(text)):
    current_char = text[char]
    if current_char not in all_chars:
        all_chars[current_char] = 1
    else:
        all_chars[current_char] += 1

for key,value in sorted(all_chars.items()):
    print(f"{key}: {value} time/s")

# text = input()
#
# all_symbols = {}
# for symbol in text:
#     all_symbols[symbol] = f": {text.count(symbol)} time/s"
#
# for key, value in sorted(all_symbols.items()):
#     print(f"{key}{value}")
#