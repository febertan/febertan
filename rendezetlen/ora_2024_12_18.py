def mysplit(mondat):
    lista = []
    i = 0
    j = 0

    while i < len(mondat):
        szo = ''

        while mondat[i] != ' ':
            szo += mondat[i]
            i += 1

        else:
            i += 1

        lista.append(szo)

    print(lista)


mysplit(input('Kérem adjon meg egy mondatot: '))
