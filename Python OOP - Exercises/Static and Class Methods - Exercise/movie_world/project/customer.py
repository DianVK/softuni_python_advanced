class Customer:

    def __init__(self, name, age, customer_id):
        self.customer_id = customer_id
        self.age = age
        self.name = name
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.customer_id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(x.name for x in self.rented_dvds)})"
