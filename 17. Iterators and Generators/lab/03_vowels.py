class vowels:
    def __init__(self, txt: str):
        self.txt = txt
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.txt):
            raise StopIteration
        if self.txt[self.index].lower() in 'aeiou':
            return self.txt[self.index]
        else:
            return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)