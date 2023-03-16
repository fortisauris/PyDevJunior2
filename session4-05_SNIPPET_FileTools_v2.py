class FileTools(object):

    @staticmethod
    def file_save(filename_w_path: str, plaintext: str):  # 'C:\ADRESAR\SUBOR'
        '''
        Nastroj na ukladanie textu do suboru
        param1::: filename_w_path - subor aj s cestou kam ho chceme ulozit
        param2::: plaintext - text vo forme stringu
        return::: None nic
        '''
        f = open(file=filename_w_path, mode='w', encoding='utf8')  # mode w znamena write zapisovanie  # latin2
        f.write(plaintext)
        print('SUBOR SA ULOZIL')
        f.close()
        return

    @classmethod
    def file_load(cls, filename_w_path: str):
        '''
        Nastroj na nacitanie textu zo suboru
        param1::: filename_w_path - subor aj s cestou odkial sa ma nacitat
        return::: nacitany_text zo suboru
        '''
        f = open(file=filename_w_path, mode='r', encoding='utf8')  # mode r znamena read
        nacitany_text = f.read()
        print(nacitany_text)
        f.close()
        return nacitany_text


    @classmethod
    def file_exist(cls, filename_w_path: str):
        """
        Jednoduchy nastroj na zistenie ci subor na disku existuje
        param1::: filename_w_path - subor aj s cestou kde sa ma subor nachadzat
        return::: True alebo False - Logicka hodnota ci subor jestvuje alebo nie
        """
        try:   # skusame kod, ktory moze vyhodit chybu
            f = open(file=filename_w_path, mode='r', encoding='utf8')
            f.read()
        except FileNotFoundError:   # zachytavame tuto chybu
            return False  # ak je chyba tak subor neexistuje a vraciame False
        finally:   # konecne tento kod sa
            pass  # kasli na to nerob nic
        return True  # ak nebola chyba vraciame  True

# HLAVNY PROGRAM
a = FileTools.file_exist(filename_w_path='session32.py')
print(a)
if a is False:
    print('SUBOR NEEXISTUJE')
else:
    print("SUBOR SA NASIEL A BUDE NACITANY")
