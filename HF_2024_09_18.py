megadott_ev = int(input('Kérem adjon meg egy évet: '))

print(5104 % 1983)
muvelet = ((megadott_ev % 1984) + 1) % 10

if muvelet == 1 or muvelet == 2:
    print('zöld')

elif muvelet == 3 or muvelet == 4:
    print('piros')

elif muvelet == 5 or muvelet == 6:
    print('sárga')

elif muvelet == 7 or muvelet == 8:
    print('fehér')

elif muvelet == 9 or muvelet == 0:
    print('fekete')