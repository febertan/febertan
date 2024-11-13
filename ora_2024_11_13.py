def atlag(atlag_list):
    osszeg = 0

    for i in range(len(atlag_list)):
        osszeg += atlag_list[i]

    atlag = osszeg / (len(atlag_list))
    return atlag


matek_list = []
magyar_list = []
tori_list = []

matek = 1

while 0 < matek <= 5:
    matek = int(input('Kérem adja meg a matek jegyeit (1-5) enterrel elválasztva, ha vége nyomjon 0-t: '))
    if matek != 0:
        matek_list.append(matek)

magyar = 1

while 0 < magyar <= 5:
    magyar = int(input('Kérem adja meg a magyar jegyeit (1-5) enterrel elválasztva, ha vége nyomjon 0-t: '))
    if magyar != 0:
        magyar_list.append(magyar)

tori = 1

while 0 < tori <= 5:
    tori = int(input('Kérem adja meg a töri jegyeit (1-5) enterrel elválasztva, ha vége nyomjon 0-t: '))
    if tori != 0:
        tori_list.append(tori)


print(atlag(matek_list))
print(atlag(magyar_list))
print(atlag(tori_list))
