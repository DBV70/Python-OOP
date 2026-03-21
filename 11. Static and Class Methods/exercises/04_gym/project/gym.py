from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subs = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subs.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subs.trainer_id), None)
        exercise = next((ex for ex in self.plans if ex.id == subs.exercise_id), None)
        equipment = next((eq for eq in self.equipment if eq.id == exercise.equipment_id), None)
        return "\n".join([subs.__str__(), customer.__str__(), trainer.__str__(), equipment.__str__(), exercise.__str__()])
