def convert_to_bin(szam):
    maradek = szam % 2
    egeszresz = szam // 2
    eredmeny = str(maradek)
    while egeszresz != 0:
        maradek = egeszresz % 2
        egeszresz = egeszresz // 2
        eredmeny = str(maradek) + eredmeny

    hossz = 0

    for _ in eredmeny:  # a pycharm problémázott, hogy a ciklusváltozó nem volt használva, és '_'-at javasolt helyére
        hossz += 1

    for _ in range(8 - hossz):
        eredmeny = '0' + eredmeny



    return eredmeny

menu = int(input('Nyomja meg az 1-es gombot ha az "a" feladatot akarja megnézni,'
                 ' és nyomja meg a 2-es gombot, ha a "b" feladatot' ))

# A feladat

if menu == 1:
    a_oktet1 = int(input('Irj be a 1. oktet értékét az ip címből (0-255): '))
    a_oktet2 = int(input('Irj be a 2. oktet értékét az ip címből (0-255): '))
    a_oktet3 = int(input('Irj be a 3. oktet értékét az ip címből (0-255): '))
    a_oktet4 = int(input('Irj be a 4. oktet értékét az ip címből (0-255): '))

    if 0 <= a_oktet1 <= 255 and 0 <= a_oktet2 <= 255 and 0 <= a_oktet3 <= 255 and 0 <= a_oktet4 <= 255:
        print('A', str(a_oktet1) + '.' + str(a_oktet2) + '.' + str(a_oktet3) + '.' + str(a_oktet4), 'ipv4 cím kettes számrendszerben kifejezve = ',
              convert_to_bin(a_oktet1) + '.' + convert_to_bin(a_oktet2) + '.' + convert_to_bin(a_oktet3) + '.' + convert_to_bin(a_oktet4))

    else:
        print('Hibás input!')

# B feladat

elif menu == 2:
    ip = input('Kérem adjon meg egy helyes ipv4 címet: ')

    b_oktet = 1
    b_oktet1 = ''
    b_oktet2 = ''
    b_oktet3 = ''
    b_oktet4 = ''

    for i in ip:
        if i == '.':
            b_oktet += 1
            continue

        if b_oktet == 1:
            b_oktet1 += i

        if b_oktet == 2:
            b_oktet2 += i

        if b_oktet == 3:
            b_oktet3 += i

        if b_oktet == 4:
            b_oktet4 += i

    b_oktet1 = int(b_oktet1)
    b_oktet2 = int(b_oktet2)
    b_oktet3 = int(b_oktet3)
    b_oktet4 = int(b_oktet4)

    if 0 <= b_oktet1 <= 255 and 0 <= b_oktet2 <= 255 and 0 <= b_oktet3 <= 255 and 0 <= b_oktet4 <= 255:
        print('A', str(b_oktet1) + '.' + str(b_oktet2) + '.' + str(b_oktet3) + '.' + str(b_oktet4), 'ipv4 cím kettes számrendszerben kifejezve = ',
              convert_to_bin(b_oktet1) + '.' + convert_to_bin(b_oktet2) + '.' + convert_to_bin(b_oktet3) + '.' + convert_to_bin(b_oktet4))

    else:
        print('Hibás input!')

else:
    print('Csak az 1-es és a 2-es között lehet választani!')