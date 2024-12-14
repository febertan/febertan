def elagazas_1():
    szam = int(input('Kérem adjon meg egy számot: '))

    if szam % 2 == 0:
        print('Páros')

    else:
        print('Páratlan')


def elagazas_2():
    szam = int(input('Kérem adjon meg egy számot: '))

    if szam > 0:
        print('Pozitív')

    elif szam < 0:
        print('Negatív')

    elif szam == 0:
        print('Nulla')


def elagazas_3():
    szamok = []
    for i in range(3):
        elem = int(input('Kérem adjon meg egy számot: '))
        szamok.append(elem)

    print(max(szamok))


def elagazas_4():
    pontszam = int(input('Kérem adja meg a pontszámot (0-100): '))

    if 0 <= pontszam <= 24:
        print('1-es')

    elif 25 <= pontszam <= 39:
        print('2-es')

    elif 40 <= pontszam <= 59:
        print('3-as')

    elif 60 <= pontszam <= 79:
        print('4-es')

    elif 80 <= pontszam <= 100:
        print('5-ös')

    else:
        print('Hibás input!')


def elagazas_5():
    jelszo = 'python123'
    jelszo2 = str(input('Kérem adja meg a jelszót: '))
    if jelszo2 == jelszo:
        print('Helyes!')

    else:
        print('Nem helyes')


def elagazas_6():
    ev = int(input('Kérem adjon meg egy évet: '))
    if ev % 4 == 0 and ev % 100 != 0 or ev % 400 == 0:
        print('Szökőév.')

    else:
        print('Nem szökőév.')


def elagazas_7():
    elso = int(input('Kérem adja meg az első oldalt:'))
    masodik = int(input('Kérem adja meg az második oldalt:'))
    harmadik = int(input('Kérem adja meg az harmadik oldalt:'))

    if elso + masodik > harmadik and elso + harmadik > masodik and masodik + harmadik > elso:
        print('Kijön')

    else:
        print('Nem jön ki')


def elgazas_8():
    szam = int(input('Kérem adjon meg egy számot: '))
    if szam % 2 == 0 and szam % 5 == 0:
        print('Páros és osztható 5-tel')

    elif szam % 2 == 0:
        print('Páros.')

    elif szam % 5 == 0:
        print('Osztható 5-tel.')

    else:
        print('Egyik se')


def elagazas_9():
    ora = int(input('Kérem adjon meg egy órát (0-23): '))
    if 0 <= ora < 6 or 22 <= ora <= 23:
        print('Éjszaka van.')

    elif 6 <= ora < 12:
        print('Reggel van.')

    elif 12 <= ora < 18:
        print('Délután vna.')

    elif 18 <= ora < 22:
        print('Este van.')

    else:
        print('Hibás input!')


def elagazas_10():
    pontszam = int(input('Kérem adja meg a pontszámát: '))
    if pontszam < 50:
        pontszam += 10

    elif 50 <= pontszam < 100:
        pontszam += 5

    print(pontszam)


def ciklus_1():
    for i in range(1, 11):
        print(i)


def ciklus_2():
    a = 10
    for i in range(10):
        print(a)
        a -= 1


def ciklus_3():
    szam = int(input('Kérem adjon meg egy számot: '))
    eredmeny = 0

    for i in range(1, szam + 1):
        eredmeny += i

    print(eredmeny)


def ciklus_4():
    for i in range(1, 11):
        print(i * 7)


def ciklus_5():
    szam = 0

    while szam < 20:
        szam += 2
        print(szam)


def ciklus_6():
    szam = int(input('Kérem adjon meg egy számot: '))
    oszto = 1
    osztok = []

    while oszto <= szam / 2:
        if szam % oszto == 0:
            osztok.append(oszto)

        oszto += 1

    osztok.append(szam)

    print(osztok[0], end='')
    for i in range(1, len(osztok)):
        print(',', osztok[i], end='')


def ciklus_7():
    lista = [3, 5, 7, 9]

    print(lista[0], end='')
    for i in range(1, len(lista)):
        print(',', lista[i], end='')


def ciklus_8():
    szam = 0
    for i in range(5):
        szam += int(input('Kérem adja meg a számot:'))

    print(szam)


def ciklus_9():
    szamok = []
    for i in range(5):
        szamok.append(int(input('Kérem adjon meg egy számot: ')))

    print(min(szamok))


def ciklus_10():
    for i in range(1, 6):
        print(i * '*')


def ciklus_11():
    szam = 4
    while szam < 50:
        print(szam)
        szam += 4


def ciklus_12():
    szo = ''

    while szo != 'stop':
        szo = input('Kérem adjon meg egy szavat: ')


def ciklus_13():  # fasgfdasgdsjgdhsgkjdshgkjdshgkj
    szam = int(input('Kérem adjon meg egy számot: '))

    a = 2
    b = 0

    if szam > 0:
        while a < ((szam / 2) + 1):
            if szam % a == 0:
                b += 1

            a += 1

    else:
        print('Nem prím.')

    if b == 0 and szam != 0:
        print('Prím.')

    else:
        print('Nem prím.')


def ciklus_14():
    szam1 = int(input('Kérem adja meg az első számot: '))
    szam2 = int(input('Kérem adja meg a második számot: '))

    if szam1 > szam2:
        while szam2 <= szam1:
            print(szam2)
            szam2 += 1

    elif szam2 > szam1:
        while szam1 <= szam2:
            print(szam1)
            szam1 += 1

    else:
        print(szam1)


def ciklus_15():
    szam = 1
    elozo_szam = 0
    eredmenyek = []
    for i in range(8):
        eredmenyek.append(elozo_szam + szam)
        elozo_szam = szam
        szam = eredmenyek[i]

    eredmenyek.append(0)
    eredmenyek.append(1)
    print(sorted(eredmenyek))


elagazas_1()
elagazas_2()
elagazas_3()
elagazas_4()
elagazas_5()
elagazas_6()
elagazas_7()
elgazas_8()
elagazas_9()
elagazas_10()
ciklus_1()
ciklus_2()
ciklus_3()
ciklus_4()
ciklus_5()
ciklus_6()
ciklus_7()
ciklus_8()
ciklus_9()
ciklus_10()
ciklus_11()
ciklus_12()
ciklus_13()
ciklus_14()
ciklus_15()
