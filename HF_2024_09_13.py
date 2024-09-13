belul_s = 2.7  #legnagyobb sebesség szerintem 50 km/h
kivul_s = 7.9  #vmax 90 km/h
autop_s = 29.7 #vmax 130 km/h

belul_t= belul_s / 50
kivul_t = kivul_s / 90
autop_t = autop_s / 130

a = round(belul_t + kivul_t + autop_t, 2)
b = round(a * 60)
i_t_perc = (8 * 60 - b)
c_ora = i_t_perc // 60
c_perc = i_t_perc % 60

print('a.) feladat: \n', 20 * '-', '\n', 'A szükséges idő az egyetemig:', a, 'óra', '\n')
print('b.) feladat: \n', 20 * '-', '\n', 'A szükséges idő az egyetimg:', b, 'perc', '\n')
print('c.) feladat: \n', 20 * '-', '\n', 'Az indulási idő:', str(c_ora) + ':' + str(c_perc))