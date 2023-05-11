class Kladivo(object):

    def __init__(self):
        self.typ = 'buracie'
        self.vaha = 5  # kg

    def buchni_kladivom(self):
        return 'BUM'

if __name__ == '__main__':
    obj = Kladivo()
    obj.vaha = 10
    print(obj.vaha)
    print(obj.buchni_kladivom())