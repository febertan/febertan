# 1. feladat

a = int(input('Kérem adjon meg egy pozitív egész számot: '))
b = int(input('Kérem adjon meg egy pozitív egész számot: '))

if a % 2 != 0:
    a += 1

c = a

print(c, end='')
c += 2

while c < b:
    print('-' + str(c), end='')
    c += 2

# 2. feladat

szam = 0
i = 1
eredmeny = 0

while szam <= 10:
    szam = int(input('Kérem adja meg a(z) ' + str(i) + '.' + ' 10-nél kisebb számot: '))
    i += 1
    eredmeny += szam

eredmeny -= szam
print('Az utolsó szám nem', str(szam) + ', nem <10-nél.')
print('A 10-nél kisebb számok összege:', eredmeny)
