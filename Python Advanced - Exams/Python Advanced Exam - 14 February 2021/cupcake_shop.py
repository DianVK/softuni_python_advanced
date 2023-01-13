def stock_availability(*args):
    inventory = [x for x in args[0]]
    parameters = args[1:]
    if parameters[-1] == "sell":
        inventory = inventory[1:]
    elif isinstance(parameters[-1], int):
        inventory = inventory[parameters[-1]:]
    else:
        for item in args[2:]:
            if parameters[0] == "delivery":
                inventory.append(item)
            elif item in inventory:
                while item in inventory:
                    inventory.remove(item)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

# from collections import deque
#
#
# def stock_availability(*args):
#     result_list = []
#     items = []
#     items_list = deque()
#     operation = []
#     operations_list = deque()
#     items.append(*args[0:1])
#     operation.append(args[1:])
#     for x in items:
#         for y in x:
#             items_list.append(y)
#     for i in operation:
#         for j in i:
#             operations_list.append(j)
#     current_operation = operations_list[0]
#     if current_operation == "delivery":
#         for stuff in range(1, len(operations_list)):
#             current_item = operations_list[stuff]
#             items_list.append(current_item)
#     elif current_operation == "sell":
#         if len(operations_list) > 2:
#             for stuff in range(len(items_list)):
#                 current_item = operations_list[stuff]
#                 items_list.append(current_item)
#
#         elif len(operations_list) == 2:
#             current_x = operations_list[1]
#             if str(current_x) not in "0123456789":
#                 for prod in items_list:
#                     if prod != current_x:
#                         result_list.append(prod)
#                 return result_list
#             else:
#                 count_products = int(operations_list[1])
#                 for q in range(count_products):
#                     items_list.popleft()
#
#         elif len(operations_list) == 1:
#             first_el = items_list[0]
#             items_list.remove(first_el)
#     final_list = []
#     for p in items_list:
#         final_list.append(p)
#     return final_list
