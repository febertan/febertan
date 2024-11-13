def bekeres():
    while 0 < targy <= 5:
        targy = int(input('Kérem adjon meg egy jegyet (1-5), kilépéshez nyomja meg a 0-t: '))
    return targy

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

print()
print('A matek átlaga:', atlag(matek_list))
print()

magyar = 1

while 0 < magyar <= 5:
    magyar = int(input('Kérem adja meg a magyar jegyeit (1-5) enterrel elválasztva, ha vége nyomjon 0-t: '))
    if magyar != 0:
        magyar_list.append(magyar)

print()
print('A magyar átlaga:', atlag(magyar_list))
print()

tori = 1

while 0 < tori <= 5:
    tori = int(input('Kérem adja meg a töri jegyeit (1-5) enterrel elválasztva, ha vége nyomjon 0-t: '))
    if tori != 0:
        tori_list.append(tori)

print()
print('A töri átlaga:', atlag(tori_list))

# a bekérést be kell rakni egy függvénybe majd
