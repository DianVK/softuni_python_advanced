def vowel_filter(func):
    vowels = "AEIOUYaeiouy"

    def wrapper():
        result = func()
        return [x for x in result if x in vowels]

    return wrapper


# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
