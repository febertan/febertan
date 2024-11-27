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


# t = []
# szamok = bekeres()
#
# while szamok != 0:
#     t.append(szamok)
#     szamok = bekeres()
#
# maxElem = t[0]
# osszeg = 0
# darab = 0
#
# for elem in t:
#     if elem > maxElem:  # max
#         maxElem = elem
#
#     osszeg += elem  # osszeg
#
#     if elem < 5:
#         darab += elem  # megszámlálás
#
# print('A legnagyobb elem:', maxElem)
# print('Összeg:', osszeg)
# print('5-nél kisebb számok: ', darab, 'db')
#
# n = len(t)
# ker = 5
# i = 0
#
# while i < n and t[i] != ker:
#     i += i
#
# if i < n:
#     print('Van ilyen', ker)
#
# else:
#     print('Nincs ilyen elem:', ker)
#
# if ker in t:
#     print('Van')
#
# else:
#     print('Nincs')
#
# i = 0
#
# while t[i] != ker:
#     i += 1
#
# print('Hányadik helyen van:', i)

# A) feladat

lista1 = [-14, 0, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77,
          100, 67, 22, 8, 17, -78, -6]

darab2 = 0
parosdb = 0
maxElem2 = lista1[0]
tiz = 0
huszonkilenc = 0
paros = True
tizenhet = 0
last_elem = lista1[0]
kovet0 = False
i = 0

for elem in lista1:
    if elem < 0:
        darab2 += 1

    if elem % 2 == 0:
        parosdb += 1

    if elem > maxElem2:
        maxElem2 = elem

    if elem % 10 == 0:
        tiz += 1

    if elem % 29 == 0 and i - huszonkilenc == i and elem != 0:
        huszonkilenc = i

    if elem % 2 != 0:
        paros = False

    if last_elem < 0 and elem == 0:
        kovet0 = True

    if elem % 17 == 0 and elem != 0:
        tizenhet = i


    last_elem = elem
    i += 1

# A/1

print('1. feladat:', len(lista1))

# A/2

if darab2 > 0:
    print('2 feladat: Igen', darab2, 'db')

else:
    print('2. feladat: Nincs')

# A/3

print('3. feladat', parosdb, 'db')

# A/4

print('4. feladat:', maxElem2)

# A/5

print('5. feladat:', tiz, 'db')

# A/6

print('6. feladat:', huszonkilenc)


# A/7

if paros is not False:
    print('7. feladat: Igaz')

else:
    print('7. feladat: Hamis')

# A/8

osszeg2 = 0

for elem in lista1:
    osszeg2 += elem

atlag = osszeg2 / len(lista1)

print('8. feladat:', round(atlag, 2), '(századra kerekítve)')

# A/9

if kovet0 is True:
    print('9. feladat: Van ilyen szám a sorozatban.')
else:
    print('9. feladat: Nincs ilyen szám a sorozatban.')


# A/10

print('10. feladat:', tizenhet)
