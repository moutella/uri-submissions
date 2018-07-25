#Nome: Abaixo da Diagonal Secundária
#Resultado: Accepted
#Data: 25/07/18 13:40:47
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
        soma+= matriz[11-j][k]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/66))
