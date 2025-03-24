import math


def elso():
    fahrenheit = int(input('Kérem adja meg a hőmérsékletet fahrenheitban: '))

    print('Celsius fokban:', 5/9 * (fahrenheit - 32))


def bekeres(x):
    return float(input(f'Kérem adja meg a {x}-t: '))


def keplet_minusz(a, b, c):
    return (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)


def keplet_plusz(a, b, c):
    return (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

# + feladat: egy függvény adja vissza mind a kettőt, ne ott printelve (változóként megadni a műveleti jelet


def masodfoku_fg():
    a = bekeres('a')
    b = bekeres('b')
    c = bekeres('c')

    if (math.sqrt(b ** 2 - 4 * a * c)) > 0:
        print('2 megoldás van:')
        print(keplet_plusz(a, b, c))
        print(keplet_minusz(a, b, c))

    elif (math.sqrt(b ** 2 - 4 * a * c) > 0) == 0:
        print('1 megoldás van:')
        print(keplet_plusz(a, b, c))

    elif (math.sqrt(b ** 2 - 4 * a * c)) > 0:
        print('0 megoldás van.')


masodfoku_fg()
