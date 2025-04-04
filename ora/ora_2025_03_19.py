def elso():
    print('A téglalap területe:',
          int(input('Kérem adja meg az egyik oldalt: ')) * int(input('Kérem adja meg a másik oldalt: ')))


def masodik():
    a = int(input('Adja meg az első számot: '))
    b = int(input('Adja meg a második számot: '))
    legnagyobb = 0

    if a > b:
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                legnagyobb = i

    else:
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                legnagyobb = i

    print(legnagyobb)


def harmadik():
    szam = int(input('Kérem adjon meg egy számot: '))
    osztok = 0

    for i in range(1, szam + 1):
        if szam % i == 0:
            osztok += 1

    print(osztok)


elso()
masodik()
harmadik()
