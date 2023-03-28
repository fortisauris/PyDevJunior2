
# ZAKLADY FUNKCIONALNEHO PROGRAMOVANIA
import functools

data = ['A', 'B', 'C', 'D', 'E', 'F']

# proceduralny pristup - tradicny
result = [] # prazdny zoznam
for i in data:
    result.append(i.lower())
print(result)

# funkcionalne programovanie je programovanie pomocou funkcii
pismena = list(map(lambda x: x.lower(), data))  #
print(pismena)

cisla = [3.5,12.65,34.78,11.87]
result = list(map(round, cisla))
print(result)

funkcia = lambda x: round(x/2)
result = list(map(funkcia, cisla))
print(result)

cisla2 = [7.54,7.243,12.87,1.87]
result = list(map(lambda x,y: x/y, cisla, cisla2))
print(result)

viac_ako_tri = list(filter(lambda x: x < 3, result))
print(viac_ako_tri)

mena = ['Gregor', 'Yveta', 'Jozef', 'Frantisek']
obsahuje_pismeno = list(filter(lambda x: 'r' in x, mena))
print(obsahuje_pismeno)

# TODO Domaca uloha spravte si aspon 3 mapy alebo filtre

redukovany_zoznam = list(functools.reduce(lambda x, y: x + y, mena))
print(redukovany_zoznam)

def spojeny_string(string1, string2):
    return string1 + string2

text = ['A', 'H', 'O', 'J']
final_string = functools.reduce(spojeny_string, text)
print(final_string)


nlist = [[1,2,3], [4,5,6], [7,8,9]]
flist = functools.reduce(lambda a,b: a+b, nlist)
print(flist)


cisla = [5435, 543, 54367, 867, 42, 876, 432, 86]
zoradeny_zoanam = sorted(cisla, reverse=True)
print(zoradeny_zoanam)

text = 'Bryndza zdrazela'
print(sorted(text.lower()))
print(sorted(text.split(' ')))

