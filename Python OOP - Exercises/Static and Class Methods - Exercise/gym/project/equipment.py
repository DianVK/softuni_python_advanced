class Equipment:
    equipment_counter = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.equipment_counter
        Equipment.equipment_counter += 1

    @staticmethod
    def get_next_id():
        return Equipment.equipment_counter

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"