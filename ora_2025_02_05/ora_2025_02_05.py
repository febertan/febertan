def data():
    adat = []
    i = 0

    with open('cb.txt', 'r', encoding='utf-8') as file:
        for row in file:
            if i != 0:
                adat.append(row.strip().split(';'))

            i += 1

    return adat


def nevek(adat):
    nev = []

    for elem in adat:
        if elem[3] not in nev:
            nev.append(elem[3])

    nev.sort()

    return nev


def elso(emberek):
    print('1. feladat')
    i = 0
    j = 0

    for elem in emberek:
        if i == 0:
            print(elem, end='')
            i += 1

        else:
            print(',', elem, end='')

        j += 1

    print(', ' + str(j) + 'db')
    print()


def masodik(adat, emberek):
    print('2. feladat')
    ki = ''
    legtobb = 0
    for nev in emberek:
        adasok = 0
        for ember in adat:
            if ember[3] == nev:
                adasok += int(ember[2])

        if adasok > legtobb:
            legtobb = adasok
            ki = nev

        elif adasok == legtobb:
            ki += nev

    print(ki + ',', legtobb, 'adással \n')


def harmadik(adat):
    print('3. feladat')
    ido = 24 * (60 ** 2)
    ki = ''

    for elem in adat:
        szamitas = ((int(elem[0]) * (60 ** 2)) + (int(elem[1]) * 60) + int(elem[2]))

        if szamitas < ido:
            ki = elem[3]
            ido = szamitas

    print(ki, '\n')


def negyedik(adat, emberek):
    print('4. feladat')

    for nev in emberek:
        adasok = 0
        for ember in adat:
            if ember[3] == nev:
                adasok += int(ember[2])

        print(nev, adasok)


elso(nevek(data()))
masodik(data(), nevek(data()))
harmadik(data())
negyedik(data(), nevek(data()))
