print('Program kezdete')
# osszeg = 0
#
# for i in range(3):
#     print('Kérem adja meg a(z)', str(i + 1) + '.', 'számot', end=' ')
#     a = int(input())
#     osszeg = osszeg + a
#
# print(osszeg)
# print('Vége')
#
# i = 0
# while i != 3:
#     print('Kérem adja meg a(z)', str(i + 1) + '.', 'számot', end=' ')
#     a = int(input())
#     osszeg = osszeg + a
# #    print(i)
#     i += 1  # i értéke 1-gyel növekszik
#
# print(osszeg)
# print('Program vége')

# 1. feladat

# szo = input('Kérem adjon meg egy szót:')
#
# while szo != 'alma':
#     print('Ez egy szép szó')
#     szo = input('Kérem adjon meg egy szót:')
#
# else:
#     print('A program futás véget ért, mert megadta a kulcsszót.')

# 2. feladat

# n = int(input('Kérem adjon meg egy számot: '))
# m = int(input('Kérem adjon meg egy másik számot: '))
#
# while m > n:
#     if n % 2 != 0:
#         n += 1
#     print(n)
#     n += 2

# 3. feladat

szam = int(input('Kérem adjon meg egy számot'))
eredeti_szam = szam
i = 1

while a < eredeti_szam:
    szam *= a
    a += 1

print(szam)