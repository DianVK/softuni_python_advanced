from itertools import permutations


def possible_permutations(nums):
    for x in permutations(nums):
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]
