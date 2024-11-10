szamok = [-4, -4, 3, 2, 4, 5, 2, 5, 2, 53, 3, 1]  # nem vagyok benne biztos, hogy magamnak kell a lista elemeit kitalálni, de nem láttam mást
szamok.sort()
cel = [szamok[0]]

for i in range(len(szamok)):
    if cel[(len(cel)) - 1] != szamok[i]:
        cel.append(szamok[i])

print(cel)
