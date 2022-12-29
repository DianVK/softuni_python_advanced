def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(),key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name,quantity in sorted_cheeses:
        result += name + "\n"
        quantity = sorted(quantity,reverse=True)
        result += "\n".join([str(el) for el in quantity]) + "\n"
    return result

# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(),key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
#     for name,quantity in sorted_cheeses:
#         print(name,end="\n")
#         quantity = sorted(quantity,reverse=True)
#         print("\n".join([str(el) for el in quantity]) + "\n")

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)