def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for x in args[1:]:
            result -= x
    elif operator == "/":
        for x in args[1:]:
            result /= x
    elif operator == "*":
        for x in args[1:]:
            result *= x
    return result


'''((((1+2)+3)+4)+5)'''
'''x = 1
eval('x+1')
2'''
print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))