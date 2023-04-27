
'''
TRANSPOZICNA SIFRA

1 2 3
4 5 6
7 8 9

3 4 5
2 9 6
1 8 7

'''

def rozdel_dlzku(seq, dlzka):
    return [seq[i:i + dlzka] for i in range(0, len(seq), dlzka)]  # list comprehension

def zakoduj(kluc, sprava):
    poradie = {
        int(val): num for num, val in enumerate(kluc)
    }
    print(poradie)

    enc_txt = ''
    for index in sorted(poradie.keys()):
        for cast in rozdel_dlzku(sprava, len(kluc)):
            try:
                enc_txt += cast[poradie[index]]

            except IndexError:
                continue

    return enc_txt


msg = 'AHOJTESTRETNEMESAVPONDELOKOSEDEMNASTEJ'
enc_msg = ''
for i in range(0,len(msg), 9):
    enc_fragment = zakoduj('630125874', msg[i:i+9])
    enc_msg += enc_fragment

print(enc_msg, '\t', msg)
