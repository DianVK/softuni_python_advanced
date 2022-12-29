def fill_the_box(*args):
    height, length, width, *data = args
    size_of_the_box = height * length * width
    no_free_space = 0
    for symbol in data:
        if symbol == "Finish":
            break
        if size_of_the_box - symbol <= 0:
            symbol -= size_of_the_box
            size_of_the_box = 0
        if size_of_the_box > 0:
            size_of_the_box -= symbol
        else:
            no_free_space += symbol

    if size_of_the_box > 0:
        return f"There is free space in the box. You could put {size_of_the_box} more cubes."

    return f"No more free space! You have {no_free_space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

# def fill_the_box(*args):
#     items = [*args]
#     height,length,width = items[0],items[1],items[2]
#     free_space = height*length*width
#     not_enough_space = False
#     left_boxes = 0
#     for item in range(3, len(items)):
#         current_item = items[item]
#         if current_item == "Finish":
#             break
#         else:
#
#             if free_space - int(current_item) >= 0:
#                 free_space -= int(current_item)
#             else:
#                 not_enough_space = True
#                 left_boxes += int(current_item)
#     if not_enough_space:
#         result = f"No more free space! You have {left_boxes} more cubes."
#     else:
#         result = f"There is free space in the box. You could put {free_space} more cubes."
#     return result