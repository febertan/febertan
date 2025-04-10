def feltoltes(oktet, hossz):
    for i in range(hossz - len(oktet)):
        oktet = '0' + oktet

    return oktet


def number_of_addresses(prefix):
    print('A hálózaton', (2 ** (32 - prefix) - 2), 'kiosztható cím van.')


def broadcast_cim(i, elso, ip, mask_oktet):
    broadcast_oktets = []

    broadcast_oktet = int(elso) + (255 - mask_oktet)

    for k in range(4):
        if k < i:
            broadcast_oktets.append(ip[k])

        elif k == i:
            broadcast_oktets.append(str(broadcast_oktet))

        else:
            broadcast_oktets.append('255')

    print('A hálózat szórási címe:', '.'.join(broadcast_oktets))


def halozati_cim(ip, mask):
    i = 0
    halozati_oktet = ''
    halozati_ipcim = []

    for elem in mask:
        if elem == 255:
            i += 1

    bin_mask_oktet = feltoltes(bin(mask[i])[2:], hossz=8)
    bin_oktet = feltoltes(bin(int(ip[i]))[2:], hossz=8)

    for j in range(8):
        if bin_oktet[j] == '1' and bin_mask_oktet[j] == '1':
            halozati_oktet += '1'

        else:
            halozati_oktet += '0'

    for k in range(4):
        if k < i:
            halozati_ipcim.append(ip[k])

        elif k == i:
            halozati_ipcim.append(str(int(halozati_oktet, 2)))

        else:
            halozati_ipcim.append('0')

    print('A hálózati azonosító címe:', '.'.join(halozati_ipcim))

    broadcast_cim(i, int(halozati_oktet, 2), ip, mask[i])


def mask(prefix):
    mask_bin = '1' * int(prefix) + '0' * (32 - int(prefix))
    i = 0
    eredmeny_bin = ''
    eredmeny = []

    for char in mask_bin:
        if i % 8 == 0 and i != 0:
            eredmeny_bin += '.'

        eredmeny_bin += char
        i += 1

    eredmeny_bin = eredmeny_bin.split('.')

    for elem in eredmeny_bin:
        oktet = int(elem, 2)
        eredmeny.append(oktet)

    return eredmeny


def ip():
    ipv4 = input('Kérem adjon meg egy ip címet (pl.: 192.168.11.5/28: ')
    oktetek = ipv4.split('.')
    utolso = oktetek[3].split('/')
    del oktetek[-1]
    oktetek.append(utolso[0])
    prefix = utolso[1]

    subnet_mask = mask(prefix)
    mask_str = []

    for elem in subnet_mask:
        mask_str.append(str(elem))

    print('Az alhálózati maszk:', '.'.join(mask_str))

    halozati_cim(oktetek, subnet_mask)
    number_of_addresses(int(prefix))


ip()