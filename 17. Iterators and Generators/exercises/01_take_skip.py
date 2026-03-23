class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.index = 0 - step

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.step
        if self.index / self.step >= self.count:
            raise StopIteration
        return self.index

numbers = take_skip(2, 6)
for number in numbers:
    print(number)