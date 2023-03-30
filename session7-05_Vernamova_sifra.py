
import os

# TPM - Trusted Platform Module -> chip vo vasom pocitaci na ulozenie kryptografickych klucov a algoritmo

print(os.urandom(12))
abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vernam_enc(sprava: str):
    '''
    Jednoduchy program na sifrovanie pomocou Vernamovej sifry a operacie XOR.
    Kluc sa generuje pomocou or.urandom()
    param1::: sprava - string na zasifrovanie
    return::: enc_sprava - zasifrovana sprava v podobe zoznamu mnoziny cisel
    '''
    kluc = os.urandom(len(sprava))  # tu generujeme kluc v podobe bytov
    pripraveny_kluc = list()  # kluc treba pred pouzitim pripravit do podoby zoznamu
    enc_sprava = list()  # tu definujeme prazdny zozname kde sa bude ukladat zasifrovana sprava
    for i in kluc:  #  pomocou cyklu prechadzame klucom
        pripraveny_kluc.append(i)  # kazdu hodnotu bytu ukldame do zoznamu hodnot kluca
    print(kluc, pripraveny_kluc)  # kontrolny print kluca a pripraveneho kluca
    for i in range(0, len(sprava)):  # pomocou cyklu prechadzame spravou aj klucom podla indexu
        enc_znak = abeceda.index(sprava[i]) ^ pripraveny_kluc[i]  # vypocitavame pomocou XOR hodnotu
        print(enc_znak)  # tlacime znak pre kontrolu
        enc_sprava.append(enc_znak)  # pridavame znak do naseho vysledneho zoznamu zasiftovanej spravy
    return enc_sprava  # vraciame z funkcie zasifrovanu spravu

print(vernam_enc('BRYNDZAZOPATDRAZELA'))  # volame funkciu

# nakolko je vzdy generovany kluc iny aj vysledok bude iny. Bez kluca sa neda text odsifrovat.
# sila sifry je postavena na nahodnosti cisel s vysokou entropiou.

# TODO spravit Decrypt
# TODO BruteForce Vernam

def vernam_dec(kluc: list, enc_sprava: list):  # rozsifrovanie
    dec_sprava = str()  # prazdna sprava
    for i in range(0, len(enc_sprava)):  # cyk
        dec_znak = kluc[i] ^ enc_sprava[i]
        dec_sprava += abeceda[dec_znak]
    return dec_sprava

kluc = [2, 226, 70, 239, 207, 190, 38, 46, 214, 183, 121, 242, 117, 246, 94, 14, 114, 122, 252]
enc_sprava = [3, 243, 94, 226, 204, 167, 38, 55, 216, 184, 121, 225, 118, 231, 94, 23, 118, 113, 252]
print(vernam_dec(kluc=kluc, enc_sprava=enc_sprava))

