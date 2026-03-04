class Calculator:
    def __init__(self, *args):
        self.numbers = args

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result

# Test code
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))