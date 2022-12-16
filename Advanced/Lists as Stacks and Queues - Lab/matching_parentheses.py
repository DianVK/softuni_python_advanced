expression = input()
braces = []
for index in range(len(expression)):
    if expression[index] == "(":
        braces.append(index)
    elif expression[index] == ")":
        start_index = braces.pop()
        print(expression[start_index:index +1])
