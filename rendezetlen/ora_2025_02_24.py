def elso():
    dictionary = {"cat": "cica", "dog": "kutya", "horse": "ló"}
    words = ['cat', 'lion', 'horse']

    for word in words:
        if word in dictionary:
            print(word, "-->", dictionary[word])
        else:
            print(word, "is not in dictionary")


def masodik():
    print()
    dictionary = {
        "cat": "cica",
        "dog": "kutya",
        "horse": "ló"
    }
    for key in dictionary.keys():
        print(key, "->", dictionary[key])

    dictionary['cat'] = 'macska'
    print(dictionary, '\n')

    dictionary['swan'] = 'hattyú'
    dictionary.update({"duck": "kacsa"})

    print(dictionary, '\n')

    del dictionary['cat']
    # del dictionary['swafn']  # -->KeyError: 'swan'
    dictionary.popitem()  # → utolsó kulcs törlés, visszatérési érték a törölt kulcs+érték tuple
    print(dictionary)
    print()

    for english, magyar in dictionary.items():
        print(english, "->", magyar)

    print()

    for magyar in dictionary.values():
        print(magyar)


def harmadik():
    print()
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.get("model")

    print(x, '\n')

    y = car.copy()

    print(y)

    z = car.pop("model")

    print(z)  # →visszatérési érték a törölt érték
    print(car)


def beker(_kulcsok, _szoveg):
    ember = {}

    for i in range(len(_kulcsok)):
        ember[_kulcsok[i]] = input('Kérem adja meg a ' + _szoveg[i] + ':')

    return ember


def elso_feladat():
    kulcsok = ['nev', 'matek', 'magyar', 'tori']
    szoveg = ['nevét', 'matek jegyét', 'magyar jegyét', 'töri jegyét', ]
    osztaly = []
    ember = {}

    for i in range(2):
        print()
        print(f'{i + 1}. tanuló adatai')
        print(30 * '_')
        osztaly.append(beker(kulcsok, szoveg))

    print(osztaly)

# elso()
# masodik()
# harmadik()
elso_feladat()
