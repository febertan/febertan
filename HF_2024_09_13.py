belul_s = 2.7  #legnagyobb sebesség szerintem 50 km/h
kivul_s = 7.9  #vmax 90 km/h
autop_s = 29.7 #vmax 130 km/h

belul_v = 50
kivul_v = 90
autop_v = 130

belul_t_h= belul_s / belul_v
kivul_t_h = kivul_s / kivul_v
autop_t_h = autop_s / autop_v

a = round(belul_t_h + kivul_t_h + autop_t_h,2)
b = round(a * 60)
i_t_perc = (8 * 60 - b)
c_ora = i_t_perc // 60
c_perc = i_t_perc % 60

print('A feladat eredménye:', a, 'óra')
print('B feladat eredménye:', b, 'perc')
print('C feladat eredménye:', str(c_ora) + ':' + str(c_perc) + '-kor kell elindulnia Dórinak.')