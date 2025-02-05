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
    nevek = []

    for elem in adat:
        if elem[3] not in nevek:
            nevek.append(elem[3])

    return nevek


def elso(nevek):
    i = 0

    for elem in nevek:
        if i == 0:
            print(elem, end='')
            i += 1

        else:
            print(',', elem, end='')

    print()


def masodik(adat, nevek):
    legtobb = 0
    nev = []
    i = 0


    for elem in adat:



    # for elem in adat:
    #     if int(elem[2]) > legtobb:
    #         legtobb = int(elem[2])
    #
    # for elem in adat:
    #     if int(elem[2]) == legtobb:
    #         nev.append(elem[3])


    print(nev, legtobb)


def harmadik(adat):
    print(adat[0][3])


elso(nevek(data()))
masodik(data(), nevek(data()))
harmadik(data())
