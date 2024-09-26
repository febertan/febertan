szam = int(input('Kérem adjon meg egy 1-nél nagyobb számot: '))
lepes = 0

while szam < 1:
    print('Hibás input')
    szam = int(input('Kérem adjon meg egy 1-nél nagyobb számot: '))

if szam % 2 == 1:
    szam += 1

while szam > 2:
    szam -= 2
    lepes += 1
    print(szam)
else:
    szam //= 2
    print(szam, '\n')
    lepes += 1  # nem vagyok benne biztos, hogy ezt is lépésnek kell számolni, de most annak számoltam

print(lepes, 'lépésből érte el az 1-et a megadott szám.')

