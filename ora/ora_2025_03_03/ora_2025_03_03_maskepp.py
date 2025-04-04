def adat():
    autok = []

    with open('autok_listaja.txt', 'r', encoding='utf-8') as file:
        for row in file:
            elemek = row.strip().split(';')
            autok.append(elemek)

    return autok


def rendezes(autok):
    i = 0
    keys = []
    vege = {}

    for row in autok:
        cars = {}
        if i == 0:
            for elem in row:
                keys.append(elem)

            i += 1

        else:
            for j in range(len(keys)):
                cars[keys[j]] = row[j]

            del cars['rendszam']

            vege[row[0]] = cars

    return vege


def feladatok(adat):
    eredmeny = 0
    koltseg = 0

    for elem in adat:
        eredmeny += int(adat[elem]['javitva'])
        koltseg += int(adat[elem]['költsége'])

    print(eredmeny, 'javítva')
    print(len(adat) - eredmeny, 'nem javítva')
    print('Összköltség:', koltseg)

    rendezett_kulcsok = sorted(adat)

    for elem in rendezett_kulcsok:
        print(elem, f'költsége:', adat[elem]['költsége'])


feladatok(rendezes(adat()))
