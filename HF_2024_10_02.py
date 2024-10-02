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


if 0 < oktet1 < 255 and 0 < oktet2 < 255 and 0 < oktet3 < 255 and 0 < oktet4 < 255:
    bin_oktet1 = bin(oktet1)[2:]
    bin_oktet2 = bin(oktet2)[2:]
    bin_oktet3 = bin(oktet3)[2:]
    bin_oktet4 = bin(oktet4)[2:]

    print(str(bin_oktet1) + '.' + str(bin_oktet2) + '.' + str(bin_oktet3) + '.' + str(bin_oktet4))

else:
    print('Hibás input!')

# 128 64 32 16 8 4 2 1

bin1_1 = oktet1 // 128
bin1_2 = oktet1 - bin1_1 * 128

bin1_3 = bin1_2 // 64
bin1_4 = bin1_2 - bin1_3 * 64

bin1_5 = bin1_4 // 32
bin1_6 = bin1_4 - bin1_5 * 32

bin1_7 = bin1_6 // 16
bin1_8 = bin1_6 - bin1_3 * 16

bin1_9 = bin1_8 // 8
bin1_10 = bin1_8 - bin1_1 * 8

bin1_11 = bin1_10 // 4
bin1_12 = bin1_10 - bin1_3 * 4

bin1_13 = bin1_12 // 2
bin1_14 = bin1_12 - bin1_1 * 2

bin1_15 = bin1_14 // 1
bin1_16 = bin1_14 - bin1_3 * 1

print(str(bin1_1) + str(bin1_3) + str(bin1_5) + str(bin1_7) + str(bin1_9) + str(bin1_11) + str(bin1_13) + str(bin1_15))
