#Nome: Menor e Posição
#Resultado: Accepted
#Data: 25/07/18 13:22:36
#Linguagem: Python 3
valor = int(input())
valores = input().split()
menor = int(valores[0])
pos = 0
for valor in valores:
    if int(valor)<menor:
        menor = int(valor)
        pos = valores.index(valor)
print("Menor valor:", menor)
print("Posicao:", pos)