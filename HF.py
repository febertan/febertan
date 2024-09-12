belul_s = 2.7  #legnagyobb sebesség szerintem 50 km/h
kivul_s = 7.9  #vmax 90 km/h
autop_s = 29.7 #vmax 130 km/h

belul_v = 50
kivul_v = 90
autop_v = 130

belul_t = belul_s / belul_v
kivul_t = kivul_s / kivul_v
autop_t = autop_s / autop_v

print(round(belul_t + kivul_t + autop_t,2))


