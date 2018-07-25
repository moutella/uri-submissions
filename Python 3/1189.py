#Nome: Área Esquerda
#Resultado: Accepted
#Data: 25/07/18 14:18:46
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(0,6):
    for j in range(k):
        soma += matriz[k][j]
        soma += matriz[11-k][j]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/30))
