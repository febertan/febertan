szo = str(input('Kérem adjon meg egy kisbetűs szót: '))
ujszo = ''

for i in range(len(szo)):
    if szo[i] != ' ':
        nb = chr(ord(szo[i]) - 32)
        ujszo += nb

    else:
        ujszo += ' '

# nb = chr(ord(szo[0]) - 32)  # mert 32-vel kisebb a betű száma ha nagy betű
# print(nb + szo[1:])
print(ujszo)
print(szo.capitalize())
print(szo.upper())