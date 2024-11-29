# B) feladat
def primszam_fg(szam):
    i = 1
    a = 0

    if szam > 0:
        while i < ((szam / 2) + 1):
            if szam % i == 0 and i != 1:
                a += 1

            i += 1


    else:
        return False

    if a == 0:
        return True

    else:
        return False


t2 = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100,
      67, 22, 8, -78, -6]

j = -1
masodik = 0
harmadik = True
negyedik_harom = 0
negyedik_ot = 0
harommal_oszthato = 0
ottel_oszhato = 0
atlag = 0
kobszam = False
negyzetszam = []
last_elem = t2[0]
nyolcadik = False
primszam = []
tizedik = 0
legnagyobb = t2[0]
masodik_legnagyobb = 0


for elem in t2:
    j += 1
    atlag += elem

    if -10 < elem < 10:
        masodik = j

    if elem > 100:
        harmadik = False

    if negyedik_harom == 0 and elem % 3 == 0:
        negyedik_harom += 1
        harommal_oszthato = elem

    if negyedik_ot == 0 and elem % 5 == 0:
        negyedik_ot += 1
        ottel_oszhato = elem

    hatodik_szam = elem
    kobgyok = 0

    while hatodik_szam >= kobgyok and kobszam == False:
        if hatodik_szam < 0:
            hatodik_szam *= -1

        if kobgyok ** 3 == hatodik_szam:
            kobszam = True

        kobgyok += 1

    negyzetgyok = 0
    hetedik_szam = elem

    if hetedik_szam < 0:
        hetedik_szam *= -1

    while hetedik_szam >= negyzetgyok:
        if negyzetgyok ** 2 == hetedik_szam:
            negyzetszam.append(negyzetgyok)

        negyzetgyok += 1

    if nyolcadik == False and last_elem > 0 and elem == 0:
        nyolcadik = True

    last_elem = elem

    if primszam_fg(elem) is True and elem != 1:
        primszam.append(elem)

    if elem > legnagyobb:
        masodik_legnagyobb = legnagyobb
        legnagyobb = elem


print('1. feladat:', j, 'eleme van.')

print('2. feladat:', j)

if harmadik is True:
    print('3. feladat: Igaz')

else:
    print('3. feladat: Hamis')

print('4. feladat: ELső hárommal osztható szám:', str(harommal_oszthato) + ', első öttel osztható szám:', ottel_oszhato)

print('5. feladat:', round(atlag / len(t2), 2)) # ha jól tudom, a számtani közép a számok átlaga

if kobszam is True:
    print('6. feladat: Igaz')
else:
    print('6. feladat: Hamis')

hetedik_eredmeny = str(negyzetszam[0])

for j in range(1, len(negyzetszam)):
    hetedik_eredmeny += ', ' + str(negyzetszam[j])

print('7. feladat:', hetedik_eredmeny)

if nyolcadik:
    print('8. feladat: Van')

else:
    print('8. feladat: Nincs')

kilencedik_eredmeny = str(primszam[0])

for k in range(1, len(primszam)):
    kilencedik_eredmeny += ', ' + str(primszam[k])

print('9. feladat:', kilencedik_eredmeny)

print('10. feladat:', masodik_legnagyobb)
