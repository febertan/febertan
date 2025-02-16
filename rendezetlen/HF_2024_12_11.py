def char_ki(szam):
    a = ''

    for betu in szam:
        if betu != '.':
            a += betu

    return a


honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus',
           'szeptember', 'október', 'november', 'december']

szamok = []

while True:
    datum_list = char_ki(input('Kérem adja meg a születési dátumát (ÉÉÉÉ/HH/NN, szóközzel elválasztva): ')).split(' ', 2)

    honap = True
    nap = True

    if datum_list[1].isdigit():
        if 0 > int(datum_list[1]) or 12 < int(datum_list[1]):
            print('Hibás hónap!')
            honap = False

    else:
        if datum_list[1].lower() not in honapok:
            print('Hibás hónap!')
            honap = False

    if int(datum_list[2]) <= 0 or int(datum_list[2]) > 31:  # ez még nem teljesen jó
        print('Hibás nap!')
        nap = False

    if nap and honap:
        break


for elem in datum_list:  # nem voltam benne biztos, hogy a hónapot számmal vagy betűvel kell-e bekérni
    if elem.isdigit():
        szamok.append(elem)

    else:
        hanyadik = honapok.index(elem.lower()) + 1
        if  hanyadik < 10:
            szamok.append('0' + str(hanyadik))

        else:
            szamok.append(hanyadik)

# print('. '.join(szamok))

print(szamok[0] + '. ' + honapok[int(szamok[1]) - 1] + ' ' + szamok[2] + '.')

osszeg = 0

for elem in szamok:
    osszeg += int(elem)

while len(str(osszeg)) != 1:
    osszeg2 = 0
    for elem in str(osszeg):
        osszeg2 += int(elem)

    osszeg = osszeg2

print(osszeg)
