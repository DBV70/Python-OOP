from .animal import Animal
from .worker import Worker

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: Worker):
        worker_to_remove = next((w for w in self.workers if worker_name == w.name), None)
        if worker_to_remove:
            self.workers.remove(worker_to_remove)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        required_budget = sum(a.money_for_care for a in self.animals)
        if self.__budget >= required_budget:
            self.__budget -= required_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def _status_by_type(self, items, type_names, header_label):
        result = [f"You have {len(items)} {header_label}"]
        for type_name in type_names:
            typed_items = [i for i in items if i.__class__.__name__ == type_name]
            result.append(f"----- {len(typed_items)} {type_name}s:")
            result.append("\n".join(str(i) for i in typed_items))
        return "\n".join(result)

    def animals_status(self):
        return self._status_by_type(self.animals, ["Lion", "Tiger", "Cheetah"], "animals")

    def workers_status(self):
        return self._status_by_type(self.workers, ["Keeper", "Caretaker", "Vet"], "workers")
