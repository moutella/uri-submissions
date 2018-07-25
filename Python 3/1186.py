#Nome: Abaixo da Diagonal Secundária
#Resultado: Wrong answer (100%)
#Data: 25/07/18 13:40:35
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(11, -1,-1):
    for j in range(0,k):
        soma+= matriz[j][11-k]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/66))
