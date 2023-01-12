from math import floor


class Integer():
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if isinstance(float_value, float):
            float_value = floor(float_value)
            return Integer(int(float_value))
        return "value is not a float"

    @staticmethod
    def from_roman(value):
        numbers = {
            'I': 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10,
            "XIX": 19
        }
        for key, val in numbers.items():
            if key == value:
                value = int(val)
                return Integer(int(value))

    @staticmethod
    def from_string(value):
        if str(value).isdigit():
            return Integer(int(value))
        else:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
