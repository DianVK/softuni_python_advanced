from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    TYPE_HORSES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = list()
        self.jockeys = list()
        self.horse_races = list()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.TYPE_HORSES:
            self.horses.append(self.TYPE_HORSES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."
