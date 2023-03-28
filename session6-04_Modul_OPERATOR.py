import operator

# tento modul obsahuje funkcie, ktore mozeme vyuzit napr v MAP FILTER SORTED


a = list(map(operator.add, [1,2,3], [5,6,7]))
print(a)

a = list(map(operator.sub, [1,2,3], [5,6,7]))
print(a)

a = list(map(operator.mul, [1,2,3], [5,6,7]))
print(a)

a,b = 423, 453
res = operator.mul(a, b)
print(res)

a,b = 1423, 453
res = operator.truediv(a, b)
print(res)

a,b = 1423, 453
res = operator.floordiv(a, b)
print(res)

a,b = 12, 34
res = operator.mod(a, b)
print(res)

a,b = 12, 3
res = operator.pow(a, b)
print(res)

# POROVNAVACIE FUNKCIE

a,b = 12, 3
res = operator.lt(a, b)  # Less Than   a < b
print(res)

a,b = 12, 3
res = operator.gt(a, b)  # greater Than   a > b
print(res)

a,b = 12, 12
res = operator.ge(a, b)  # greater or equal    a >= b
print(res)

a, b = 12, 12
res = operator.le(a, b)  # less or equal    a <= b
print(res)

a,b = 12, 12
res = operator.eq(a, b)  # equal    a == b
print(res)

if operator.eq(a, b):   # a == b
    print('ROVNAKE HODNOTY')

a,b = 12, 1
res = operator.ne(a, b)  # non equal    a != b
print(res)

"""
BITWISE OPERACIE - 0b00000000- 0b1111111  - 0x00 do 0xff
"""

a = 255
res = operator.invert(a)  # otocil znamienka
print(res)

# res = operator.contains(mena, 'Frantisek')  # TODO chyba mena
# print(res)
