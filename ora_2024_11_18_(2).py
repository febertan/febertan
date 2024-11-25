def paros_e(szam_fg):
    if szam_fg % 2 == 0:
        return True


def kilep(a):
    if a != 0:
        return True


def osszeg_fg(osszeg_fg):
    osszeg = 0
    for i in range(len(osszeg_fg)):
        osszeg += osszeg_fg[i]

    return osszeg


def atlag(ossz, szamok):
    hossz = len(szamok)
    eredmeny = ossz / hossz

    return eredmeny

osszeg = 0
szam = int(input('Kérem adjon meg egy számot: '))
szamok = []


while kilep(szam) == True:
    szamok.append(szam)
    osszeg = osszeg_fg(szamok)


    if paros_e(szam) is True:
        print('A szám páros.')
    else:
        print('A szám páratlan.')

    szam = int(input('Kérem adjon meg egy számot: '))

print(atlag(osszeg, szamok))
