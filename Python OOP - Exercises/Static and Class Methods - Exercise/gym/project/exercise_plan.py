class ExercisePlan:
    exercise_plan_counter = 1

    def __init__(self,trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.exercise_plan_counter
        ExercisePlan.exercise_plan_counter += 1

    @classmethod
    def from_hours(cls,trainer_id:int, equipment_id:int, hours:int):
        hours_to_minutes = hours * 60
        return cls(trainer_id,equipment_id,hours_to_minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_plan_counter

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
