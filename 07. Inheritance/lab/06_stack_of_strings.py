class Stack:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f"[{', '.join(reversed(self.data))}]"

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data
