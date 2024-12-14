# nev = str(input('Kérem adjon meg egy nevet: '))
# nev_list = []
#
# for i in range(len(nev)):
#     # print(nev[i], ' --> ', ord(nev[i]))
#     nev_list.append(ord(nev[i]) + 1)
#
# print(nev_list)
#
# i = 0
#
# for elem in nev_list:
#     print(chr(elem), end='')
#
# print()
#
# for elem in nev_list:
#     print(nev[i], ' --> ', elem - 1)
#     i += 1

# 1.) feladat

szo = str(input('Kérem adjon meg egy szót: '))

for i in range(len(szo)):
    print(szo[i], end=' ')

print('\n')

for i in range(0, len(szo), 2):
    print(szo[i])

print()

for i in range(len(szo)):
    print(ord(szo[i]))

