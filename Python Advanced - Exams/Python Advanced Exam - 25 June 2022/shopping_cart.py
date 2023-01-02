def shopping_cart(*args):
    stuff = {'Pizza': [], 'Soup': [], 'Dessert': []}
    for items in args:
        eats = items[0]
        product = items[1]
        if items == 'Stop':
            break
        if eats == 'Pizza' and len(stuff['Pizza']) == 4:
            continue
        elif eats == 'Soup' and len(stuff['Soup']) == 3:
            continue
        elif eats == 'Dessert' and len(stuff['Dessert']) == 2:
            continue
        if product not in stuff[eats]:
            stuff[eats].append(product)

    for value in stuff.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(stuff.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for items in sorted_cart:
        result += f"{items[0]}:\n"
        sorted_product = sorted(items[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))