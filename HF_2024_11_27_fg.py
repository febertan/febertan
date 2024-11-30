def elso(lista):
    return len(lista)


def masodik_fg(szam, hanyadik):
    index = 0

    if -10 < szam < 10:
        index = hanyadik

    return index


def harmadik_fg(szam):
    if szam > 100:
        return False

    else:
        return True


def negyedik_harom_fg(szam):
    if szam % 3 == 0:
        return szam

    else:
        return True


def negyedik_ot_fg(szam):
    if szam % 5 == 0:
        return szam

    else:
        return True


def otodik(lista):
    atlag = sum(lista) / len(lista)

    return round(atlag, 2)


def hatodik_fg(szam):
    kobgyok = 0

    if szam < 0:
        szam *= -1

    while kobgyok <= szam:
        if szam == kobgyok ** 3:
            return True

        kobgyok += 1

    else:
        return False


def hetedik_fg(szam, lista):
    negyzetgyok = 0

    if szam > 0:
        while negyzetgyok <= szam:
            if negyzetgyok ** 2 == szam:
                lista.append(negyzetgyok)

            negyzetgyok += 1

    return lista


def nyolcadik_fg(elozo, szam):
    if szam == 0 and elozo > 0:
        return True

    else:
        return False


def kilencedi_fg(szam):
    a= 2
    b = 0

    if szam > 0:
        while a < ((szam / 2) + 1):
            if szam % a == 0:
                b += 1

            a += 1


    else:
        return False

    if b == 0:
        return True

    else:
        return False


def tizedik_fg(lista):
    lista.sort()

    return lista[len(lista) - 2]



t2 = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100,
      67, 22, 8, -78, -6]

i = 0
masodik = 'Nincs ilyen szám.'
harmadik = True
negyedik_harom = True
negyedik_ot = True
hatodik = False
hetedik = []
last_elem = t2[0]
nyolcadik = False
kilencedik = []

for elem in t2:
    masodik = str(masodik_fg(elem, i))

    if harmadik:
        harmadik = harmadik_fg(elem)

    if negyedik_harom is True:
        negyedik_harom = negyedik_harom_fg(elem)

    if negyedik_ot is True:
        negyedik_ot = negyedik_ot_fg(elem)

    if hatodik is False:
        hatodik = hatodik_fg(elem)

    hetedik = hetedik_fg(elem, hetedik)

    if not nyolcadik:
        nyolcadik = nyolcadik_fg(last_elem, elem)

    if kilencedi_fg(elem) is True and elem != 1:
        kilencedik.append(elem)

    i += 1
    last_elem = elem

print('1. feladat:', elso(t2))
print('2. feladat:', masodik) # feltételezem, hogy az indexek 0-tól kezdődnek

if harmadik:
    print('3. feladat: Igaz')

else:
    print('3. feladat: Hamis')

print('4. feladat: Első hárommal osztható szám:', negyedik_harom, '\n',
      '           Első öttel osztható szám:', negyedik_ot)

print('5. feladat:', otodik(t2))

if hatodik:
    print('6. feladat: Igaz')

else:
    print('6. feladat: Hamis')

hetedik_eredmeny = str(hetedik[0])

for j in range(1, len(hetedik)):
    hetedik_eredmeny += ', ' + str(hetedik[j])

print('7. feladat:', hetedik_eredmeny)

if nyolcadik:
    print('8. feladat: Van')

else:
    print('8. feladat: Nincs')

kilencedik_eredmeny = str(kilencedik[0])

for k in range(1, len(kilencedik)):
    kilencedik_eredmeny += ', ' + str(kilencedik[k])

print('9. feladat:', kilencedik_eredmeny)

print('10. feladat:', tizedik_fg(t2))
