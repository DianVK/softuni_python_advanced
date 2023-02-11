class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self,people):
        if not self.is_taken and self.capacity + self.guests > people:
            self.is_taken = True
            self.guests += people
            return

        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"


