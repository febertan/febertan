def adat():
    hegyek = []
    i = 0

    with open('hegyekMo.txt', 'r', encoding='utf-8') as file:
        for row in file:
            if i == 0:
                i += 1

            else:
                elemek = row.strip().split(';')
                hegyek.append(elemek)

    return hegyek


def elso():
    print('1. feladat')
    szam = int(input('Kérem adjon meg egy egész számot: '))

    if szam % 2 == 0:
        print('Páros a szám')

    else:
        print('Nem páros')


def darabolas(nev):
    ekezet = ['á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ú']
    sima = ['a', 'e', 'i', 'o', 'o', 'o', 'u', 'u', 'u']
    nev2 = ''

    for elem in nev:
        if elem in ekezet:
            index = ekezet.index(elem)
            betu = sima[index]
            nev2 += betu

        else:
            nev2 += elem

    return nev2


def email(vezeteknev, keresztnev, osztaly):
    vez = darabolas(vezeteknev.lower())
    ker = darabolas(keresztnev.lower())
    oszt = osztaly.split('.')
    kezdes_ev = 2024 - int(oszt[0]) + 8  # mert 2024-ben kezdődött az év

    print(f'{vez}.{ker}.tech{kezdes_ev}{oszt[1].lower()}@bolyaimovar.com')


def harmadik_b(hegyek):
    legkisebb = 10000
    legkisebb_nev = ''

    for row in hegyek:
        if int(row[2]) < legkisebb:
            legkisebb = int(row[2])
            legkisebb_nev = row[0]

    print(legkisebb, legkisebb_nev)


def harmadik_c(hegyek):
    osszeg = 0
    oszto = len(hegyek)

    for row in hegyek:
        osszeg += int(row[2])

    print(round(osszeg / oszto, 2))


def harmadik_d(hegyek):



# elso()
email(vezeteknev='Buga', keresztnev='Jakab', osztaly='12.B')
harmadik_b(adat())
harmadik_c(adat())
