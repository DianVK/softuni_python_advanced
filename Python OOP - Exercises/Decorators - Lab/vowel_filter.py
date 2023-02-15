def vowel_filter(function):
    all_vowels = "AaEeIiOoUuYy"

    def wrapper():
        result = function()
        return [x for x in result if x in all_vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
