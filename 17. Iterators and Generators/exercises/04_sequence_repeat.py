class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.number:
            idx = self.index % len(self.sequence)
            self.index += 1
            return self.sequence[idx]
        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')