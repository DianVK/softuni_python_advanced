class Calculator:

    @staticmethod
    def add(*args):
        sum_all = 0
        for x in args:
            sum_all += x
        return sum_all

    @staticmethod
    def multiply(*args):
        multiply_all = 1
        for x in args:
            multiply_all *= x
        return multiply_all

    @staticmethod
    def divide(*args):
        divide_all = args[0]
        for x in range(1, len(args)):
            divide_all /= args[x]
        return divide_all

    @staticmethod
    def subtract(*args):
        subtract_all = args[0]
        for x in range(1, len(args)):
            subtract_all -= args[x]
        return subtract_all


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))