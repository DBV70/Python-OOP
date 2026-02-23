x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        return x

    def change_global():
        x = "global: changed!"
        return x

    print("outer:", x)  #2
    print("inner:", inner())
    print("outer:", inner()) # 4
    print(change_global())

print(x)
outer()