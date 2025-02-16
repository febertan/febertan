# 1. feladat

# szo = input('Adjon meg egy szót: ')
#
# if szo == 'tűzliliom':
#     print('Ezt ismerem, ez egy csodaszép virág!')
#
# else:
#     print('Ez nagyon szép szó!')

# 2 . feladat

jovedelem = float(input('Kérem adja meg az éves jövedelmét euróban: '))

ado = 0

if jovedelem < 14400:
    ado = 0.0
    maradt = jovedelem - ado
    print('Önnek nem kell adót fizetnie.')

elif 14400 <= jovedelem < 34000:
    ado = jovedelem * 0.19
    maradt = jovedelem - ado
    print('Önnek 19% adót kell fizetnie.')

elif jovedelem >= 34000:
    ado = jovedelem * 0.29
    maradt = jovedelem - ado
    print('Önnek 29% adót kell fizetnie. \n',
          maradt, 'pénze marad.')

# 3. feladat

magassag = float(input('Kérem adja meg a magasságát m-ben:'))
tomeg = float(input('Kérem adja meg a testtömegét kg-ban:'))

m2 = magassag ** 2
tti = round(tomeg / m2, 2)

# 18,5 – 25 	normális testsúly

print(30 * '*' + 5*'-' + 30 * '*')
print('Az ön testtömegindexe:', tti, '%')

if tti < 18.5:
    print('sovány')

elif 18.5 <= tti < 25:
    print('normál')

elif 25 <= tti < 30:
    print('túlsúlyos')

elif 30 <= tti:
    print('elhízott')