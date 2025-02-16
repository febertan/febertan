def harommal_oszthatok(lista):
    db = 0
    for i in range(len(lista)):
        if lista[i] % 3 == 0 and lista[i] != 0:
            db += 1

    return db


szam = input('Kérem adjon meg egy számot: ')
szamok = []

while szam != '':
    szamok.append(int(szam))
    szam = input('Kérem adja meg a következő számot: ')

print(harommal_oszthatok(szamok), 'db 3-mal osztható számot adott meg.')
