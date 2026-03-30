from project.collectors.base_collector import BaseCollector

class PrivateCollector(BaseCollector):
    INITIAL_MONEY = 25000.0
    INITIAL_SPACE = 3000

    def __init__(self, name):
        super().__init__(name, self.INITIAL_MONEY, self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 5000.0