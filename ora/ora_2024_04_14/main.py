# M = semmi
# E = ugyan anyit előre ugrik mint dobott
# V = ugyan annyit ugrik vissza mint dobott (nem megy sehova)

def osvenyek():
    osveny = []

    with open('osvenyek.txt', 'r', encoding='utf-8') as file:
        for row in file:
            osveny.append(row.strip().split('/n'))

    return osveny


def dobasok():
    dobas = ''

    with open('dobasok.txt', 'r', encoding='utf-8') as file:
        for elem in file:
            for char in elem:
                if char.isdigit():
                    dobas += char

    return dobas


def masodik():
    print('2. feladat')
    print('A dobások száma:', len(dobasok()))
    print('Az ösvények száma:', len(osvenyek()))


def harmadik(osvenyek):
    print('3. feladat')
    leghosszabb_sorszam = 0
    leghosszabb_hossz = 0
    i = 0

    for row in osvenyek:
        if len(row[0]) > leghosszabb_hossz:
            leghosszabb_sorszam = i
            leghosszabb_hossz = len(row[0])

        i += 1

    print(f'Az egyik leghosszabb a(z) {leghosszabb_sorszam + 1}. ösvény, hossza: {leghosszabb_hossz}')


def negyedik(osvenyek):
    print('4. feladat')
    szamok = []

    osveny_szama = int(input('Adja meg egy ösvény sorszámát: ')) - 1

    while osveny_szama + 1 > len(osvenyek) or osveny_szama < 0:
        print('Túl nagy érték!')
        osveny_szama = int(input('Adja meg egy ösvény sorszámát: ')) - 1

    jatekosok_szama = int(input('Adja meg a játékosok számát (2-5): '))

    while 2 > jatekosok_szama or 5 < jatekosok_szama:
        print('2-től 5-ig terjedhet csak a játékosok száma!')
        jatekosok_szama = int(input('Adja meg a játékosok számát (2-5): '))

    szamok.append(osveny_szama)
    szamok.append(jatekosok_szama)

    return szamok


def otodik(osvenyek, adatok):
    print('5. feladat')
    osveny_szama = adatok[0]
    mezok = {'M': 0, 'V': 0, 'E': 0}

    for row in osvenyek[osveny_szama]:
        for char in row:
            if char == 'M':
                mezok['M'] += 1

            elif char == 'V':
                mezok['V'] += 1

            elif char == 'E':
                mezok['E'] += 1

    for key in mezok.keys():
        if mezok[key] > 0:
            print(f'{key}: {mezok[key]} darab')


def hatodik(osveny):
    with open('kulonleges.txt', 'w', encoding='utf-8') as file:
        i = 0
        sor = []

        for row in osveny:
            for char in row:
                if char == 'E':
                    sor.append(i)
                    sor.append('E')

                if char == 'V':
                    sor.append(i)
                    sor.append('V')

            i += 1

        if len(sor) > 0:
            file.write(f'{sor[0]}. mező, {sor[1]}')



masodik()
harmadik(osvenyek())
adatok = negyedik(osvenyek())  # osveny szama, jatekosok szama
otodik(osvenyek(), adatok)
hatodik(osvenyek()[adatok[0]])  # ez még nem jó
