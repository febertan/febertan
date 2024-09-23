print('Program kezdete')
osszeg = 0

# for i in range(3):
#     print('Kérem adja meg a(z)', str(i + 1) + '.', 'számot', end=' ')
#     a = int(input())
#     osszeg = osszeg + a
#
# print(osszeg)
# print('Vége')

i = 0
while i != 3:
    print('Kérem adja meg a(z)', str(i + 1) + '.', 'számot', end=' ')
    a = int(input())
    osszeg = osszeg + a
#    print(i)
    i += 1  # i értéke 1-gyel növekszik

print(osszeg)
print('Program vége')
