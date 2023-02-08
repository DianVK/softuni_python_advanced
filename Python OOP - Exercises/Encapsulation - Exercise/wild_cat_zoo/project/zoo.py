from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity >= len(self.animals) + 1:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity >= len(self.animals) + 1:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker:Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for pos, x in enumerate(self.workers):
            if x.name == worker_name:
                del self.workers[pos]
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum(x.salary for x in self.workers)
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_costs = 0
        for animal in range(len(self.animals)):
            current_animal = self.animals[animal]
            total_costs += current_animal.money_for_care
        if self.__budget >= total_costs:
            self.__budget -= total_costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        info = {"Cheetah": [], "Tiger": [], "Lion": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]
        result = [f"You have {len(self.animals)} animals",
                  f"----- {len(info['Lion'])} Lions:", *info['Lion'],
                  f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
                  f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]
        return "\n".join(result)

    def workers_status(self):
        info = {"Keeper": [], "Vet": [], "Caretaker": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]
        result = [f"You have {len(info['Keeper']) + len(info['Vet']) + len(info['Caretaker'])} workers",
                  f"----- {len(info['Keeper'])} Keepers:", *info['Keeper'],
                  f"----- {len(info['Caretaker'])} Caretakers:", *info['Caretaker'],
                  f"----- {len(info['Vet'])} Vets:", *info['Vet']]
        return "\n".join(result)
