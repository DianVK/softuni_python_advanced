def math_operations(*args,**kwargs):
    operators = kwargs
    numbers = [*args]
    counter = 0
    for item in numbers:
        if counter == 4:
            counter = 0
        counter += 1
        if counter == 1:
            operators['a'] += item
        elif counter == 2:
            operators['s'] -= item
        elif counter == 3 and int(item) != 0:
            operators['d'] /= item
        elif counter == 4:
            operators['m'] *= item
    for item,value in sorted(operators.items(),key=lambda x: (-x[1], -len(x[0]), x[0])):
        print(f"{item}: {value:.1f}")

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))