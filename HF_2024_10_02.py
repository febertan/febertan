ip = 0

# for i in range(4):
#     i += 1
#     print('Adja meg egy ipv4-es ip cím', str(i) + '. részét: ', end='')
#     szam = int(input())


# print(bin(szam)[2:]) ezt nem tanultuk

oktet1 = int(input('Kérem ajda meg az ipv4 cím első oktetét: '))
oktet2 = int(input('Kérem ajda meg az ipv4 cím második oktetét: '))
oktet3 = int(input('Kérem ajda meg az ipv4 cím harmadik oktetét: '))
oktet4 = int(input('Kérem ajda meg az ipv4 cím negyedik oktetét: '))

if oktet1 > 255 and oktet2 > 255 and oktet3 > 255 and oktet4 >255:
    bin_oktet1 = bin(oktet1)[2:]
    bin_oktet2 = bin(oktet2)[2:]
    bin_oktet3 = bin(oktet3)[2:]
    bin_oktet4 = bin(oktet4)[2:]

    print(str(bin_oktet1) + '.'
          + str(bin_oktet2) + '.'
          + str(bin_oktet3) + '.'
          + str(bin_oktet4))
