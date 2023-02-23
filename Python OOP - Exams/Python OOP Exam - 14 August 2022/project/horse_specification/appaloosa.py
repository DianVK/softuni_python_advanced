from horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + 2 > self.MAX_SPEED else self.speed + 2
