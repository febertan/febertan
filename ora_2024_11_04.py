gyumolcs = ['alma', 'körte', 'banán']

print(gyumolcs[1])
# print(gyumolcs[10])       IndexError: list index out of range

print('----')

for i in range(3):
    print(gyumolcs[i])

print('----')

lista2 = ['353', '242', '35', ['egy', 'kettő', 'három']]
print(lista2[3][2])

print('----')

lista3 = [10, 12, 25, 4, 9, 13]
hossz1 = len(lista3)
osszeg1 = 0
for i in range(hossz1):
    osszeg1 += lista3[i]

print(osszeg1)

print('----')

lista4 = ['hétfő ', 'kedd', 'szerda', 'Július', 'csütörtök', 'péntek']

lista4.append('szombat')
print(lista4)

lista4.insert(1, 'narancs')
print(lista4)

print('----')

# lista5 = []
#
# a = -1
# while a != 0:
#     a = int(input('Kérem adjon meg egy egész számot:'))
#
#     lista5.append(a)
#
# osszeg2 = 0
# for i in range(len(lista5)):
#     osszeg2 += lista5[i]
#
# print(osszeg2)
#
# print('----')

# 1. feladat

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június',
      'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
t3 = []
for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)

# 2. feladat

# b = 1
# for i in range(len(t2)):
#     t2.insert(b, '*')
#     b += 2
#
# for i in range(len(t2)):
#     print(t2[i], end=' ')

for i in range(len(t2)):
    if i != (len(t2) - 1):
        print(t2[i], end=' * ')

    else:
        print(t2[i])
