def data():
    adat = []
    i = 0

    with open('vadaszterulet.csv', 'r', encoding='utf-8') as file:
        for row in file:
            if i != 0:
                adat.append(row.strip().split(';'))

            i += 1

    for i in range(3):
        del adat[-1]

    return adat


def cimkulon(adat):
    uj_adat = []

    for row in adat:
        varos = ''
        szam = ''
        i = 0
        j = 0

        for elem in row[0]:
            if i == 0:
                varos += elem

            if i == 3:
                szam += elem

            if i == 1 or i == 2:
                i += 1

            if j == 0 and elem == '/':
                j += 1
                i += 1

        varos = varos[:-1]
        del row[0]

        row.insert(0, szam)
        row.insert(0,varos)
        uj_adat.append(row)

    print(uj_adat)


cimkulon(data())

# szam eltárolása egy lefutásig, és ha ugyan az mint az előző terület összeadása
