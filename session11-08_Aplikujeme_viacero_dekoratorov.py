
def decor1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decor2(func):
    def wrapper():
        x = func()
        return x * 2
    return wrapper

@decor1
@decor2
def cislo():
    return 10

print(cislo())