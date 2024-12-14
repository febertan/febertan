honapok = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus',
           'szeptember', 'október', 'november', 'december']

datum_list = input('Kérem adja meg a születési dátumát (ÉÉÉÉ.HH.NN): ').split('.', 2)

szamok = []

for elem in datum_list:  # nem voltam benne biztos, hogy nem úgy kell bekérni, hogy hónapot számmal is lehet kérni
    if elem.isdigit():
        szamok.append(elem)

    else:
        hanyadik = honapok.index(elem) + 1
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
