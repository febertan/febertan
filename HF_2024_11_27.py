# B) feladat

t2 = [-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, -61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100,
      67, 22, 8, -78, -6]

i = -1
masodik = 0
harmadik = True

for elem in t2:
    i += 1

    if -10 < elem < 10:
        masodik = i

    if elem > 100:
        harmadik = False



print('1. feladat:', i, 'eleme van.')
print('2. feladat:', i)

if harmadik is True:
    print('3. feladat: Igaz')

else:
    print('3. feladat: Hamis')


print('4. feladat:')
print('5. feladat:')
print('6. feladat:')
print('7. feladat:')
print('8. feladat:')
print('9. feladat:')
print('10. feladat:')
