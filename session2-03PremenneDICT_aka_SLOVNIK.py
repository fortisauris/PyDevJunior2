# SLOVNIK

zoznam_zoznamov = list()
zoznam_zoznamov.append(['maslo', 'chlieb'])
zoznam_zoznamov.append(['kecup', 'paradajky'])
print(zoznam_zoznamov)

chladnicka = dict()   # {'key':'value'}
chladnicka['policka1'] = ['horcica', 'kecup']
chladnicka['policka2'] = ['chren', 'majoneza']
chladnicka['aktualna_teplota'] = 7.05  # stupne celzia
chladnicka['zatvorene_dvere'] = True
print(chladnicka)
print(chladnicka['policka1'])

b = dict()
b['aktualna_teplota'] = 7.35
b['dvere'] = ['mlieko', 4637, 646, 543]
chladnicka.update(b)
print(chladnicka)

print(chladnicka['aktualna_teplota'])
print(chladnicka.get('aktualna_teplota'))

print(chladnicka.keys())
print(chladnicka.values())
