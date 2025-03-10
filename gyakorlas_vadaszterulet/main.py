def to_float(szam):
    eredmeny = ''

    for char in szam:
        if char == ',':
            eredmeny += '.'

        else:
            eredmeny += char

    return float(eredmeny)


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

    return uj_adat


def terulet(data):
    i = 0
    last_row = []
    new_last_row = []

    for row in data:
        i += 1

        if last_row[1] == row[1]:
            terulet = to_float(last_row[5]) + to_float(row[5])

            del last_row[5]

            new_last_row = last_row.insert(5, '')  # ezt megoldani, hogy csak az utolsó sorban legyen ott a terület, ez még nem teljes

        last_row = row


terulet(cimkulon(data()))


# szam eltárolása egy lefutásig, és ha ugyan az mint az előző terület összeadása
