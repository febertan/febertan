lista = []
i = 0
a = 0
b = 0

while i < 10:
    number = input('Szám: ')

    if number.isdigit() is False:
        print('Számot!')

    else:
        lista.append(int(number))
        i += 1

print(max(lista))
print(sum(lista))

for j in lista:
    if j % 2 == 0:
        a += 1

print(f'{a}db páros szám van.')

for k in lista:  #nem jó még, csak lusta vagyok befejezni mert unalmas.
    for l in range(1, k // 2):
        if k % l != 0 and k != l and l != 1:
            b = b
        else:
            b += 1

if b != 0:
    print('Van közöttük prím')

else:
    print('Nincs közöttük prím')
