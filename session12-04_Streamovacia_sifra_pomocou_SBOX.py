'''
STREAMOVACIA SIFRA ZALOZENA NA SBOXE
'''

def sbox_enc(sbox, key):
    # pismena v premennej abeceda 26 znakov
    key = ord(key)  # ord nam meni znaky podla tabulky znakov na cisla
    # print(key)
    # enc_znak = int()
    for i in sbox:
        key ^= i
        #print(i, key)
    return key


# TODO Prestavka do 19:50

msg = 'BRYNDZA ZDRAZELA'
sbox = [23,56,89,235,127,90,87,55]

enc_msg = []  # list()
for key in msg:
    enc_key = sbox_enc(sbox, key)
    #print(enc_key)
    enc_msg.append(enc_key)

print(enc_msg)

# TODO SBOX OPACNY -- DESIFROVANIE - funkcia na otacanie SBOXU

