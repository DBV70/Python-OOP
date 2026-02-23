class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        if damage >= self.health:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            self.health -= damage
            return None

    def heal(self, amount: int):
        self.health += amount
        return None

# Test code
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
