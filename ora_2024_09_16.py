# elso = input('Kérem adja meg az első számot:')
# masodik = input('Kérem adja meg a második számot:')
#
# print(elso, masodik)

# 1. feladat

vezetekn = input('Kérem adja meg a vezetekevét:')
keresztn = input('Kérem adja meg a keresztenvét:')
szuletesiEv = int(input('Kérem adja meg a születési évét:'))

import datetime
jelenlegiEv = datetime.datetime.now().year
kor = jelenlegiEv - szuletesiEv

print('Az ön teljes neve:', vezetekn, keresztn)
print('Az életkora:', kor, 'év')

# 2. feladat

print('Kérem adja meg az esemény kezdő időpontjának adatait:')

start_h = int(input("óra:"))
start_m = int(input("perc:"))
idotart = int(input('Esemény időtartam (perc):'))

a = int((start_h * 60) + start_m + idotart)
end_h = str(a // 60)
end_m = str(a % 60)

print(30 * '*')
print('Az esemény', end_h + ':' + end_m + '-ig tart')

# 3. feladat

belul_s = float(input('Hány km-t tesz meg településen belül?'))  # legnagyobb sebesség szerintem 50 km/h
kivul_s = float(input('Hány km-t tesz meg településen kívül?'))  # vmax 90 km/h
autop_s = float(input('Hány km-t tesz meg autópályán?'))  # vmax 130 km/h

belul_v = 50
kivul_v = 90
autop_v = 130

belul_t = belul_s / belul_v
kivul_t = kivul_s / kivul_v
autop_t = autop_s / autop_v

a = round(belul_t + kivul_t + autop_t, 2)
b = round(a * 60)
i_t_perc = (8 * 60 - b)
c_ora = i_t_perc // 60
c_perc = i_t_perc % 60

print('Településen belül', str(belul_v) + 'km/h-val ment,',
      'településen kívül', str(kivul_v) + 'km/h-val ment,',
      'autópályán meg', str(belul_v) + 'km/h-val.')
print('a.) feladat: \n', 20 * '-', '\n', 'A szükséges idő az egyetemig:', a, 'óra', '\n')
print('b.) feladat: \n', 20 * '-', '\n', 'A szükséges idő az egyetimg:', b, 'perc', '\n')
print('c.) feladat: \n', 20 * '-', '\n', 'Az indulási idő:', str(c_ora) + ':' + str(c_perc))
