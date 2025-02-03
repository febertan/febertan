def data():
    adat = []
    with open('parduc_2.txt', 'r', encoding='utf-8') as vers:
        for row in vers:
            if row != '\n':
                a = row.strip().split(' ')
                adat.append(a)

        return adat


def elso(data_elso):
    hossz = 0

    for elem in data_elso:
        for elem2 in elem:
            for elem3 in elem2:
                if elem3.isalpha():
                    hossz += 1

    print('A vers hossza:', hossz, 'karakter.')


def masodik(data_masodik):
    maganhangzo = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    darab = 0

    for elem in data_masodik:
        for elem2 in elem:
            for elem3 in elem2:
                if elem3.lower() in maganhangzo:
                    darab += 1

    print(darab, 'magánhangzó van a versben.')


def harmadik(data_harmadik):
    darab = 0
    nemszo = ['.', '?', '!', ',', '-', ':', ' ']

    for elem in data_harmadik:
        for elem2 in elem:
            if elem2 not in nemszo: # nincs tesztelve
                darab += 1

    print(darab)


elso(data())
masodik(data())
harmadik(data())
