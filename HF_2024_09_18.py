megadott_ev = int(input('Kérem adjon meg egy évszámot 1984 és 2043 között: '))

ev_sorszam = ((megadott_ev % 1984) + 1) % 10
# működik a megadott tartományon kívül is, csak a feladatba azt mondta, hogy legyen ez megadva
# ev_sorszam = ((megadott_ev - 1984) % 10 + 1)  ezzel működik 1984 alatt is

if 1984 <= megadott_ev <= 2043:
        if ev_sorszam == 1 or ev_sorszam == 2:
                print('zöld')

        elif ev_sorszam == 3 or ev_sorszam == 4:
                print('piros')

        elif ev_sorszam == 5 or ev_sorszam == 6:
                print('sárga')

        elif ev_sorszam == 7 or ev_sorszam == 8:
                print('fehér')

        elif ev_sorszam == 9 or ev_sorszam == 0:
                print('fekete')

else:
    print('Az évszám nincs a megadott tartományon belül')
