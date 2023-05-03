'''
Doteraz sme spustali pythonovke skripty takto:

'''


def hello():
    return 'hello'

print('HELLO')  # ak funkciu hello nainportujeme do dalsieho skriptu tak sa tento kod VYKONA co nechceme
print(hello())  # chceme iba nainportovat funkciu hello()

''''
Odteraz budeme pouzivat podmienku, ze kod sa vykona iba ked subor spustime ako hlavny subor __main__

aby sa nam vykonal iba kod, ktory chceme a nie vsetko co je sucastou skriptu
'''

if __name__ == '__main__':
    print(hello())  # ak funkciu hello nainportujeme do dalsieho skriptu tak sa tento kod NEVYKONA !!!
    # spusti iba ked ho spustime ako hlavny.