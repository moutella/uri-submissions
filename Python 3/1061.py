#Nome: Tempo de um Evento
#Resultado: Accepted
#Data: 24/07/18 18:45:28
#Linguagem: Python 3
diaInicio = int(input().split()[1])
horaInicio = input().split()
diaFim = int(input().split()[1])
horaFim = input().split()
dias = diaFim - diaInicio
horaDif = int(horaFim[0])-int(horaInicio[0])
minFim = int(horaFim[2])-int(horaInicio[2])
segFim = int(horaFim[4])-int(horaInicio[4])

if segFim < 0:
    minFim -= 1
    segFim += 60
if minFim < 0:
    horaDif -= 1
    minFim+=60
if horaDif < 0:
    horaDif+=24
    dias -= 1
print("{} dia(s)".format(dias))
print("{} hora(s)".format(horaDif))
print("{} minuto(s)".format(minFim))
print("{} segundo(s)".format(segFim))
