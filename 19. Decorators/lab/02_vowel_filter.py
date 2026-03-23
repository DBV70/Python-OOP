def vowel_filter(func):
    def wrapper():
        result = func()
        return [el for el in result if el.lower() in "aeiouy"]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())