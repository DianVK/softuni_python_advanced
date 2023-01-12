from room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        [room.take_room(people) for room in self.rooms if room.number == room_number]

    def free_room(self, room_number):
        [room.free_room() for room in self.rooms if room.number == room_number]

    def status(self):
        self.guests = 0
        free_rooms, taken_rooms = [], []
        for x in self.rooms:
            if x.is_taken:
                taken_rooms.append(str(x.number))
                self.guests += x.guests
            else:
                free_rooms.append(str(x.number))
        output = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(free_rooms)}",
                  f"Taken rooms: {', '.join(taken_rooms)}"]

        return "\n".join(output)

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
