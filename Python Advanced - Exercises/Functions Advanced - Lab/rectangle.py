def rectangle(length, width):
    if not all([isinstance(x, int) for x in [length, width]]):
        return "Enter valid values!"
    #def check_valid(length,width):
    #check_length,check_width = isinstance(length, int),isinstance(width, int)
    #if not check_length or not check_width:
    #    def rectangle(length, width):
    #        if not all([isinstance(x, int) for x in [length, width]]):
    #            return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))