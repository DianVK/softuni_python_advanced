from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product: Product):
        for x in self.products:
            if x.__class__.__name__ == product.__class__.__name__:
                return x

    def remove(self, product_name):
        for pos, x in enumerate(self.products):
            if x.name == product_name:
                del self.products[pos]

    def __repr__(self):
        result = ""
        for item in self.products:
            result += f"{item.name}: {item.quantity}\n"
        return result.rstrip()
