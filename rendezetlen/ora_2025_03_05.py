def elso():
    ember = {'név': 'Géza', 'születési_év': 1999, 'lakhely': 'Makkoshotyka', 'foglalkozás': 'szarvasmarha-tenyésztő',
             'szemei száma': 2, 'kedvenc lottószámok': [1, 2, 3, 4, 5]}

    for elem in ember:
        print(elem)

    print()

    for elem in ember:
        print(ember[elem])

    print()

    for elem in ember:
        print(elem + ':' + str(ember[elem]))

    print()

    print(ember['név'])

    ember['kutya'] = 'Bodri'

    del ember['szemei száma']

    ember['születési_év'] = 1980

    print(ember)


def masodik():
    konyvek = []
    konyv = {}

    while True:
        # itt van a probléma, hogy a listában üres lesz a szerzo
        konyv['szerző'] = input('Kérem adjon meg egy szerzőt, hagyja üresen a kilépéshez: ')

        if konyv['szerző'] == '':
            break

        konyv['cím'] = input('Kérem adja meg a könyv címét: ')

        konyvek.append(konyv)

    print(konyvek)


# elso()
masodik()
