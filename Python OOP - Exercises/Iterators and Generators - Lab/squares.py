def squares(num: int):
    first_num = 1
    while first_num <= num:
        yield first_num ** 2
        first_num += 1


print(list(squares(5)))
