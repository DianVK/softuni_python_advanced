def rectangle(length, width):
    if not all([isinstance(x, int) for x in [length, width]]):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"