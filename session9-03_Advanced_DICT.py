'''
ADVANCED DICTIONARY - SLOVNIK
'''


a = dict()
a = dict(one=1, two=2, three=3)
print(a)

b = {'one':1,
     'two':2,
     'three':3
     }

print(b)
print(type(b['one']))

c = dict(zip(['one', 'two', 'three'], [1,2,3]))
print(c)
print(list(c))
print(len(c))

print(c['one'])


c['Srobovak'] = None
print(c['Srobovak'])
c['four'] = 4
print(c)

del c['four']
print(c)

print('one' in c)
print('Srobovak' not in c)

a = iter(c)
for i in range(0, len(c)):
    key = next(a)
    print(i, key, c[key])


c.clear()
print(c)

c = b.copy()  # plytka kopia
print(c)
vystup = c.fromkeys(c.keys())
print(vystup)

print(c['one'])
print(c.get('one'))
print(c)

print(c.keys())
print(c.values())
print(c.items())

for i in c.items():
    print(i[0], i[1])

c.pop('one')
print(c)

val = c.popitem()
print(val, '\t', c)
val = c.popitem()
print(val, '\t', c)

c = b
print(c)
c_it = reversed(c)  # otoceny iterator
# print(c_it)
print(next(c_it))
print(c_it.__next__())
print(c_it.__next__())
# print(c_it.__next__())  # vyhodi chybu stop iteration

c.update(b)
print(c)


# dictview objects
print(len(c.items()))

# TODO Prestavka do 19:50

a = iter(c.keys())
for i in range(0, len(c.keys())):
    print(next(a))

print('one' in c.keys())
print(False in c.values())  # TODO preskumame preco to tak robi
print(c)

a = reversed(c.items())
print(next(a))
