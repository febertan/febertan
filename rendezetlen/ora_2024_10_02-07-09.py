# 1. feladat

# a = int(input('Kérem adjon meg egy pozitív egész számot: '))
# b = int(input('Kérem adjon meg egy pozitív egész számot: '))
#
# if a % 2 != 0:
#     a += 1
#
# c = a
#
# print(c, end='')
# c += 2
#
# while c < b:
#     print('-' + str(c), end='')
#     c += 2

# 2. feladat

# szam = 0
# i = 1
# eredmeny = 0
#
# while szam <= 10:
#     szam = int(input('Kérem adja meg a(z) ' + str(i) + '.' + ' 10-nél kisebb számot: '))
#     i += 1
#     eredmeny += szam
#
# eredmeny -= szam
# print('Az utolsó szám nem', str(szam) + ', nem <10-nél.')
# print('A 10-nél kisebb számok összege:', eredmeny)

# 3. feladat

a = float(input('Kérem adja meg a háromszög "a" oldalának a hosszát: '))
b = float(input('Kérem adja meg a háromszög "b" oldalának a hosszát: '))
c = float(input('Kérem adja meg a háromszög "c" oldalának a hosszát: '))
s = (a + b + c) / 2

while a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a + b > c and a + c > b and b + c > a:
        print('A hárömszög megszerkeszthető!')
        break
else:
    print('A háromszög nem megszerkeszthető')
    a -= a
    b -= b
    c -= c
    a += float(input('Kérem adja meg a háromszög "a" oldalának a hosszát: '))
    b += float(input('Kérem adja meg a háromszög "b" oldalának a hosszát: '))
    c += float(input('Kérem adja meg a háromszög "c" oldalának a hosszát: '))

T = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 1)
K = round(s * 2, 1)
print('A hárömszög területe:', T, 'A háromszög kerülete:', K)

# Ez nem jó

# 4. feladat
