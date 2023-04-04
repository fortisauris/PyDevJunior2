
'''
ADVANCED LIST
'''
a= list()
print(type(a))

a.append('Jergus')  # pridaj na koniec
print(a)

print(dir(a))

a.extend(['Maros', 'Roman'])  # pridaj zoznam do zoznamu
print(a)

a.insert(2, 'Yveta')  # vlozime na index 2 Yvetu
print(a)

a.remove('Maros')  # odstranime Marosa
print(a)

if "Andrej" in a:  # podmienka nebola splnena
    a.remove('Andrej')
print(a)

# while True:
meno = a.pop(1)  # vytiahni a vymaz zo zoznamu
print(meno, a)

a.clear()  # vymaze zoznam
# del a  # vymaze objekt
print(a)


fruits = ['Banany', 'Jablka', 'Ananas', 'Kiwi', 'Jablka']
print(fruits.index("Jablka", 0, len(fruits)))  # clen zoznamu, zaciatok kde ma hladat a koniec
if 'Srobovak' in fruits:
    print(fruits.index("Srobovak", 0, len(fruits)))  #
else:
    print('Ziaden srobovak tu nie je')

print(fruits.count('Jablka'))

fruits.sort(reverse=True)  # nemozeme dat do printu lebo sa nam vrati None
print(fruits)

fruits.reverse()  # modifikuje objekt v pamati a vracia None
print(fruits)

fruits2 = fruits.copy()  # shallow copy plytka kopia
print(fruits2)
print(id(fruits))
print(id(fruits2))
print(id(fruits[0]))
print(id(fruits2[0]))

fruits2.insert(0, 'Srobovak')
print(fruits2)
print(id(fruits2[0]))

# stack
stack = [1,2,3,4,5]
print(stack.pop())
print(stack.pop())
stack.append(6)
print(stack)

del stack[:]
print(stack)

from collections import deque, ChainMap

queue = deque(['Anton', 'Jozef', 'Matus'])
queue.append('Yveta')
print(queue)
print(dir(queue))
queue.popleft()
print(queue)
queue.appendleft('Zuzana')
print(queue)

alpha = [1,2,3,4,5,6]
beta = ['Alpha','Beta', 'Gama']
a = ChainMap(alpha, beta)
print(type(a))
print(a)
for i in a:
    print(i)
