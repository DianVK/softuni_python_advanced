def number_increment(numbers):

    def increase():
        for num in range(len(numbers)):
            numbers[num] += 1
        return numbers
    return increase()


print(number_increment([1, 2, 3]))

# def number_increment(numbers):
#     def increase():
#         return [el + 1 for el in numbers]
#
#     return increase()
