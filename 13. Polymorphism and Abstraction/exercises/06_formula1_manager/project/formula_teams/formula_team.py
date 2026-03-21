from abc import ABC, abstractmethod

class FormulaTeam(ABC):
    MIN_BUDGET = 1000000
    def __init__(self, budget: int):
        self.__budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value: int):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def team_data(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors, expenses = self.team_data
        revenue = 0
        for sponsor in sponsors.values():
            for position, price in sponsor.items():
                if race_pos <= position:
                    revenue += price
                    break
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
