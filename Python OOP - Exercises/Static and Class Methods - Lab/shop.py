class Shop:

    def __init__(self, name: str, shop_type: str, capacity: int):
        self.capacity = capacity
        self.shop_type = shop_type
        self.name = name
        self.items = {}

    @staticmethod
    def small_shop(name: str, shop_type: str):
        return Shop(name, shop_type, 10)

    def add_item(self, item_name: str):
        if self.capacity > sum(self.items.values()):
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] - amount < 0:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] <= 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.shop_type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

# class Shop:
#
#     def __init__(self, name: str, type_shop: str, capacity: int):
#         self.name = name
#         self.type_shop = type_shop
#         self.capacity = capacity
#         self.items = {}
#
#     @classmethod
#     def small_shop(cls, name: str, type_shop: str):
#         return cls(name, type_shop, 10)
#
#     def add_item(self,item_name:str):
#         if item_name not in self.items and self.capacity > len(self.items):
#             self.items[item_name] = 1
#             return f"{item_name} added to the shop"
#         else:
#             self.items[item_name] += 1
#             return f"{item_name} added to the shop"
#
#     def remove_item(self, item_name:str, amount:int):
#         if item_name in self.items:
#             if self.items[item_name] >= amount:
#                 self.items[item_name] -= amount
#                 if self.items[item_name] == 0:
#                     del self.items[item_name]
#                 return f"{amount} {item_name} removed from the shop"
#         return f"Cannot remove {amount} {item_name}"
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type_shop} with capacity {self.capacity}"