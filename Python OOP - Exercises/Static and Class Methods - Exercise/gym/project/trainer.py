class Trainer:
    trainer_counter = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.trainer_counter
        Trainer.trainer_counter += 1

    @staticmethod
    def get_next_id():
        return Trainer.trainer_counter

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
