from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls,stars_count:int):
        new_ins = f"{stars_count} stars Hotel"
        return cls(new_ins)

    def add_room(self, room: Room):
        self.rooms.append(room)
        return

    def take_room(self,room_number, people):
        [room.take_room(people) for room in self.rooms if room.number == room_number]
        # for room in self.rooms:
        #     if room == room_number:
        #         room.take_room(people)

    def free_room(self,room_number):
        [room.free_room() for room in self.rooms if room == room_number]

    def status(self):
        self.guests = 0
        free_rooms, taken_rooms = [], []
        for x in self.rooms:
            if x.is_taken:
                taken_rooms.append(str(x.number))
                self.guests += x.guests
            else:
                free_rooms.append(str(x.number))

        output = f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
        return output

