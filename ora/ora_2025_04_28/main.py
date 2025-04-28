def adat():
    adatok = []

    with open('autok.txt', 'r', encoding='utf-8') as file:
        for row in file:
            adatok.append(row.strip().split(' '))

    return adatok


def masodik(adatok):
    print('2. feladat')

    i = -1

    while True:
        if adatok[i][-1] == '0':
            print(f'{adatok[i][0]}. nap rendszám: {adatok[i][2]}')
            break

        i -= 1


def harmadik(adatok):
    print('3. feladat')

    nap = input('Nap: ')
    print(f'Forgalom a(z) {nap}. napon:')
    for elem in adatok:
        if elem[0] == nap:
            if elem[-1] == 0:
                allapot = 'ki'

            else:
                allapot = 'be'

            print(elem[1], elem[2], elem[3], allapot)


def negyedik(adatok):
    bent = []
    kint = []
    i = -1

    for _ in range(len(adatok)):
        if adatok[i][-1] == '0' and adatok[i][2] not in kint and adatok[i][2] not in bent:
            kint.append(adatok[i][2])

        if adatok[i][-1] == '1' and adatok[i][2] not in kint and adatok[i][2] not in bent:
            bent.append(adatok[i][2])

        i -= 1

    print(bent, kint)


masodik(adat())
# harmadik(adat())
negyedik(adat())
