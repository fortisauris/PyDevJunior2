
class Ryba(object):
    '''
    tato trieda nam ukazuje jednoduchy model ryby
    '''

    def __init__(self, latinsky_nazov: str, voda: str):
        self.nazov = latinsky_nazov
        self.voda = voda
        print('RYBA MENOM', self.nazov, 'ZIJE V', self.voda)

    def plava(self):
        '''
        Jednoducha metoda triedy, ktora umoznuje nasej rybe plavat ked tuto metodu zavolame. Vyuzijeme cyklus FOR
        aby plavala 5x za sebou
        :return:
        '''
        for i in range(5):
            print('PLAVA')
        return


kapor = Ryba(latinsky_nazov='Cyprinus carpio', voda='rybnik')
print(kapor.nazov)
kapor.plava()
