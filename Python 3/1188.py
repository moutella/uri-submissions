#Nome: Área Inferior
#Resultado: Accepted
#Data: 25/07/18 13:59:03
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(11, 6, -1):
    for j in range(-(k-6),k-6):
        soma+= matriz[k][j+6]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/30))
