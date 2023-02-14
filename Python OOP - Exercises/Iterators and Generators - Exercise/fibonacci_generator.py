def fibonacci():
    now_num = 1
    old_num = 0

    while True:
        yield old_num
        old_num, now_num = now_num, old_num + now_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

# generator = fibonacci()
# for i in range(1):
#     print(next(generator))


# def fibonacci():
#     n1, n2 = 0, 1
#
#     while True:
#         yield n1
#
#         n1, n2 = n2, n1 + n2
