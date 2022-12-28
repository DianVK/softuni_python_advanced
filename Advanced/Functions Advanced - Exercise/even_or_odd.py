def even_odd(*args):
    nums = list()
    operation = ""
    for x in args:
        if str(x).isdigit():
            nums.append(x)
        else:
            operation += x
    if operation == "even":
        result = list(filter(lambda x: x % 2 == 0,nums))
        return result
    elif operation == "odd":
        result = list(filter(lambda x: x % 2 != 0, nums))
        return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))