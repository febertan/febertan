def atlag(atlag_list):
    osszeg = 0
    for i in range(len(atlag_list)):
        osszeg += atlag_list[i]

    if osszeg != 0:
        eredmeny = osszeg / len(atlag_list)

    else:
        eredmeny = 0
    return round(eredmeny, 1)


def beker(targy, sorszam=1):
    jegyek = []
    jegy = int(input('Kérem adja meg a(z) ' + str(sorszam) + '. tantárgy (' + targy + ') jegyeit (1-5), 0-t ha vége: '))
    while jegy != 0:
        jegyek.append(jegy)
        jegy = int(input('Kérem adja meg a(z) ' + str(sorszam) + '. tantárgy (' + targy + ') jegyeit (1-5), 0-t ha vége: '))

    return atlag(jegyek)


print('Kérem adja meg a matek jegyeket.')
matek = beker(targy='matek', sorszam=1)
tori = beker(targy='töri', sorszam=2)
magyar = beker(targy='magyar', sorszam=3)

print('Matek:', matek, 'átlag:')
print('Töri:', tori, 'átlag:')
print('Magyar:', magyar, 'átlag:')
