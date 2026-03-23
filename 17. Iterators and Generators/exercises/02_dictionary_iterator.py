class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict_tuple) -1:
            self.index += 1
            return self.dict_tuple[self.index]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)