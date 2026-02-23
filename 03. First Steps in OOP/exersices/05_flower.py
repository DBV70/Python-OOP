class Flower:
    def __init__(self, name:str, water_requirements:int):
        self.name = name
        self.water_requirements = water_requirements

    is_happy = False

    def water(self, qty):
        self.is_happy = qty >= self.water_requirements

    def status(self):
        return f"{self.name} is {'happy' if self.is_happy else 'not happy'}"

# Test code
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())