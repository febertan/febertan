szam = int(input('Írj be egy pozitív egész számot: '))
oszto = 2
oszto_mennyiseg = 0
szam_fele = szam // 2

while oszto <= szam_fele:
    if (szam % oszto) == 0:
        print('Az', int(oszto), 'osztója a', str(szam) + '-nek')
        oszto_mennyiseg += 1

    oszto += 1

if oszto_mennyiseg == 0:
    print('A', szam, 'Prímszám')
