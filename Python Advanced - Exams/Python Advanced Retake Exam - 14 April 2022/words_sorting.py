def words_sorting(*args):
    result = ""
    items = {}
    for word in args:
        if word not in items:
            items[word] = 0
            total_score = 0
            for char in word:
                total_score += ord(char)
            items[word] = total_score
    sum = 0
    for value in items.values():
        sum += value
    if sum % 2 == 0:
        for item,value in sorted(items.items(),key=lambda x: (x[1], len(x[0]), x[0])):
            result += f"{item} - {value}\n"
    else:
        for item,value in sorted(items.items(),key=lambda x: (-x[1], -len(x[0]), x[0])):
            result += f"{item} - {value}\n"
    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
