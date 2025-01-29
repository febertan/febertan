def adattarolas():
    import csv
    adatok = []

    with open('eu.csv', newline='', encoding='utf-8') as stadionok:
        reader = csv.reader(stadionok, delimiter=',')

        for row in reader:
            adatok.append(row)

    return adatok


def adattarolas_2():
    eu = []
    with open('eu.csv', 'r', encoding='utf-8') as source:
        for row in source:
            country = row.strip().split(',')
            eu.append(country)

    return eu


def elso(tagok):
    evszamok = []
    i = 0

    for elem in tagok:
        evszamok.append(elem[2])

    for elem in tagok:
        if elem[2] == min(evszamok):
            i += 1

    print(i, 'darab alapítóországa van az EU-nak')


def masodik(tagok):
    for elem in tagok:
        if (elem[1][0]).capitalize() == 'B':
            print(elem[0])


def harmadik(tagok):
    orszagok = []

    for elem in tagok:
        orszagok.append(elem[0])


# print('EU fővárosok:')
# for elem in adattarolas_2():
#     print(elem[1], end=', ')

elso(adattarolas_2())
masodik(adattarolas_2())
harmadik(adattarolas_2())
