segundos = int(input())

# Horas:
resh = segundos % 360
#horas = int((segundos - resh) / 360)

# Minutos:
resm = resh % 60
#minutos = int((resh - resm) / 60)

# Segundos:
#segundos = resm

#print("{}:{}:{}".format(horas, minutos, segundos))



minutos = int(segundos / 60)
segundos = int(segundos - (minutos * 60))

horas = int(minutos / 60)
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))