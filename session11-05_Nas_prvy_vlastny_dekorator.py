def hello(func):

    def wrapper():  # toto jhe vnutorna funkcia
        print('UROB VOLACO PRED VLOZENO FUNKCIOU')  # skontroloval nieco
        func()
        print('UROB VOLACO PO VYKONANI FUNKCIE')  # poupratoval po sebe

    return wrapper

@hello
def nasa_funkcia():
    print('UROB VOLACO')

# HLAVNY PROGRAM
nasa_funkcia()