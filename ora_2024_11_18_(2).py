def paros_e(szam_fg):
    if szam_fg % 2 == 0:
        return True


def osszeg_fg(osszeg_fg):
    return osszeg_fg


szam = int(input('Kérem adjon meg egy számot: '))

while szam != 0:
    osszeg = []


    if paros_e(szam) is True:
        print('A szám páros.')
    else:
        print('A szám páratlan.')

    szam = int(input('Kérem adjon meg egy számot: '))

