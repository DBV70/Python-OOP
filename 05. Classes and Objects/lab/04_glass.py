class Glass:
    capacity = 250
    def __init__(self):
        self.content = 0

    def fill(self, quantity):
        if self.capacity - self.content >= quantity:
            self.content += quantity
            return f"Glass filled with {quantity} ml"
        return f"Cannot add {quantity} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"

# Test code
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())