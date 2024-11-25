def bekeres():
    szam = int(input('Kérem adjon meg egy számot, ha végzett 0-t: '))

    return szam


# def maxelem(szamok_max):
#     max = szamok_max[0]
#     for i in range(len(szamok_max)):
#         if szamok_max[i] > max:
#             max = szamok_max[i]
#
#     return max
#
#
# t = []
# szamok = bekeres()
#
# while szamok != 0:
#     t.append(szamok)
#     szamok = bekeres()
#
# print('A legnagyobb elem:', maxelem(t))


t = []
szamok = bekeres()

while szamok != 0:
    t.append(szamok)
    szamok = bekeres()

maxElem = t[0]
osszeg = 0
darab = 0

for elem in t:
    if elem > maxElem:  # max
        maxElem = elem

    osszeg += elem  # osszeg

    if elem < 5:
        darab += elem  # megszámlálás

print('A legnagyobb elem:', maxElem)
print('Összeg:', osszeg)
print('5-nél kisebb számok: ', darab, 'db')

n = len(t)
ker = 5
i = 0

while i < n and t[i] != ker:
    i += i

if i < n:
    print('Van ilyen', ker)

else:
    print('Nincs ilyen elem:', ker)

if ker in t:
    print('Van')

else:
    print('Nincs')

i = 0

while t[i] != ker:
    i += 1

print('Hányadik helyen van:', i)

# 1.) feladat

lista1 = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
          100, 67, 22, 8, -78, -6]

# 1/1

print('1. feladat:', len(t))

# 1/2

darab2 = 0
parosdb = 0
maxElem2 = lista1[0]
tiz = 0
huszonkilenc = 0
paros = True

for elem in lista1:
    if elem < 0:
        darab2 += 1

    if elem % 2 == 0:
        parosdb += 1

    if elem > maxElem2:
        maxElem2 = elem

    if elem % 10 == 0:
        tiz += 1


    if elem % 2 != 0:
        paros = False


print('2 feladat:', darab2, 'db')

# 1/3

print('3. feladat', parosdb, 'db')

# 1/4

print('4. feladat:', maxElem2)

# 1/5

print('5. feladat:', tiz, 'db')

# 1/6

print()


# 1/7

if paros == False:
    print('Hamis')

else:
    print('Igaz')

# 1/8

osszeg2 = 0

for elem in lista1:
    osszeg += elem

atlag = osszeg2 / len(lista1)

# 1/9


