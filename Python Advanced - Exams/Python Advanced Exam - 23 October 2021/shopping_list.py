def shopping_list(budget,**kwargs):
    global products
    if budget < 100:
        return "You do not have enough budget."
    result = ""
    while budget >= 100:
        products = []
        for product,info in kwargs.items():
            price = float(info[0])
            quantity = int(info[1])
            current_item_sum = quantity * price
            if budget >= current_item_sum:
                bought_item = f"{str(product)} - {current_item_sum:.2f}"
                products.append(bought_item)
                budget -= current_item_sum
                if len(products) >= 5:
                    break
            if len(products) >= 5:
                break
        if len(products) >= 5:
            break
    for item in products:
        product_name,product_price = item.split(" - ")
        result += f"You bought {product_name} for {product_price} leva.\n"

    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))