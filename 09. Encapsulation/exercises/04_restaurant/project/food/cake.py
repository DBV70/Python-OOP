from project.food.dessert import Dessert

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
    def _init_(self, name, price = PRICE, grams = GRAMS, calories = CALORIES):
        super().__init__(name, price, grams, calories)
