szam = int(input('Kérem adjon meg egy 1-nél nagyobb számot: '))
lepes = 0

while szam < 1:
    print('Hibás input')
    szam = int(input('Kérem adjon meg egy 1-nél nagyobb számot: '))

while szam > 1:
    if szam % 2 == 0:
        szam //= 2  # azért osztok így, hogy int maradjon, mert a maradék úgyis mindig 0 lesz
    else:
        szam += 1

    lepes += 1
    print(szam)

# lépésnek vettem azt is, amikor elérte az 1-et
print(lepes, 'lépésből érte el az 1-et a megadott szám.')
