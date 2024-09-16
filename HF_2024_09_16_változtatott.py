magassag = float(input('Kérem adja meg a magasságát cm-ben:'))
tomeg = float(input('Kérem adja meg a testtömegét kg-ban:'))

m2 = (magassag / 100) ** 2
tti = round(tomeg / m2, 2)

# 18,5 – 25 	normális testsúly
min_t = round(18.5 * m2, 2)
max_t = round(25 * m2, 2)

print(30 * '*' + 5*'-' + 30 * '*')
print('Az ön testtömegindexe:', tti, '%')
print('Az ön magasságához az ideális tömeg', min_t, 'kg és', max_t, 'kg között van')