def type_check(num_type):
    def decorator(func):
        def wrapper(num):
            if isinstance(num, num_type):
                return func(num)
            return "Bad Type"
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))