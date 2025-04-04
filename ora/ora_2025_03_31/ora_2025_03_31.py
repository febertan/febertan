def elso():
    while True:
        mondat = input('Kérem adjon meg egy mondatot legvégén írásjellel (. ? !), kilép: ')

        if mondat == '':
            break

        if mondat[-1] == '.':
            print('Kijelentő mondat.')

        if mondat[-1] == '?':
            print('Kérdő mondat.')

        if mondat[-1] == '!':
            print('Felkiáltó / felszólító / óhajtó mondat.')


def harmadik():
    eletkor = []

    for i in range(2):
        nev = input('Kérem adjon meg egy nevet: ')
        eletkor.append(int(input(f'Kérem adja meg {nev} életkorát: ')))

    print(f'Ketten együtt {sum(eletkor)} évesek.')


def maszk(prefix):
    # végig menni 8 számonként, és 128/2-vel szorozni (64/2, 32/2...), és ezt összeadogatni
    print()


def ip():
    ipv4 = input('Kérem adjon meg egy ip címet (pl.: 192.168.11.5/28: ')
    oktet = ''
    oktetek = []
    per = 0
    prefix = ''

    for char in ipv4:
        if char == '/':
            per += 1
            oktetek.append(oktet)

        if char == '.':
            oktetek.append(oktet)
            oktet = ''

        if char != '.' and per == 0:
            oktet += char

        if per != 0:
            prefix += char

    prefix = int(prefix)
    maszk(prefix)



# elso()
# harmadik()
ip()
