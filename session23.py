'''
SESSION 23 - FUNKCIE NA TESTOVANIE POMOCOU UNITEST A PYTEST

'''

# import unittest



def give_me_five():

    def set_status():
        return True

    global status
    status = set_status()
    return 5

def get_status():
    global status
    print(status)
    return status


if __name__ == '__main__':
    a = give_me_five()
    print(a)
    get_status()