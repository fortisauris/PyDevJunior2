class NasaTrieda(object):  # TOTO JE LEN PLANIK NASEHO OBJEKTU !!!

    '''
    Toto je funkcny model objektu skolskej triedy. TOTO JE LEN PLANIK TRIEDY
    '''

    def __init__(self):
        print("VZNIKLA NASA TRIEDA")
        self.menny_zoznam = list()  # zoznam ziakov
        self.pocet_hodin = int()
        self.zoznam_predmetov = list()

    def pocet_ziakov(self):
        '''
        Vrati dlzku menneho zoznamu
        :return: integer
        '''
        return len(self.menny_zoznam)

    def je_ziakom_triedy(self, meno_ziaka):
        '''
        Tato metoda zistuje ci je ziak clenom nasej triedy
        :param meno_ziaka:
        :return: Bool
        '''
        return meno_ziaka in self.menny_zoznam

    def vypis_ziakov(self):
        '''
        vypise menny zoznam ziakov pod seba
        :return: None
        '''
        for i in self.menny_zoznam:
            print(i)
        return


tretiabe = NasaTrieda()  # tu sa narodila nasa trieda
tretiabe.menny_zoznam = ['Peter', 'Jozef', 'Anicka', 'Zuzana']
tretiabe.menny_zoznam.append('Frantisek')
print(tretiabe.pocet_ziakov())
tretiabe.vypis_ziakov()
tretiabe.zoznam_predmetov = ['anglictina', 'matematika']
print(tretiabe.zoznam_predmetov)
print(tretiabe.je_ziakom_triedy('Alan'))
druhace = NasaTrieda()  # tu sa narodila druhace
druhace.menny_zoznam = ['Zuzana',
                        'Jozefina',
                        'Artur']
druhace.menny_zoznam.append('Alan')
print('JE ZIAKOM', druhace.je_ziakom_triedy('Zuzana'))
print(tretiabe.je_ziakom_triedy('Alan'))

