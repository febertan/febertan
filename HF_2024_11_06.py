szamok = [-4, 3, 2, 4, 5, 2, 5, 2, 53, 3, 1]  # nem vagyok benne biztos, hogy magamnak kell a lista elemeit kitalálni, de nem láttam mást
cel = [szamok[0]]

for i in range(len(szamok)):
    benne = 0
    for j in range(len(cel)):
        if cel[j] == szamok[i]:
            benne = 1

    if benne == 0:
        cel.append(szamok[i])

cel.sort()
print(cel)
