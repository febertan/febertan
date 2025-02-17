def keres():
    print('Kérem adjon meg egy pozitív egész számot: ', end='')


def osszeg():
    eredmeny = 0
    for _ in range(len(szamok)):
        eredmeny += szamok[i]

    return eredmeny


szamok = []

for i in range(3):
    keres()
    szam = int(input())
    szamok.append(szam)

print('A számok összege: ', osszeg())
