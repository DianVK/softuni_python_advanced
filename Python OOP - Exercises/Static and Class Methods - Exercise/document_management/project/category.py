class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def edit(self, new_name: str):  # – edit the name of the category
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
