br_acad_hours = int(input ('Please, enter the number of academical hours:')) #enter 64
minutes=(br_acad_hours*40) + (br_acad_hours//3*15)
astro_hours=minutes//60
type_hours = 'Astronomical_hours'
print (f'{type_hours} : {astro_hours}')
