from project.food.food import Food

class Dessert(Food):
    GRAMS = 22
    def __init__(self, name, price, calories: float, grams = GRAMS):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value