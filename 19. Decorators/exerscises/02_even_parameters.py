def even_parameters(func):
    def wrapper(*args, **kwargs):
        if any(not isinstance(arg, int) or arg % 2 != 0 for arg in args):
            return "Please use only even numbers!"
        return func(*args, **kwargs)
    return wrapper

@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))