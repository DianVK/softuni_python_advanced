class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


class Children:
    @staticmethod
    def play():
        return "Children are playing"


def start_playing(obj):
    return obj.play()


guitar = Guitar()
print(start_playing(guitar))

children = Children()
print(start_playing(children))
