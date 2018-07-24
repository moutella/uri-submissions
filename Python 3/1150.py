#Nome: Ultrapassando Z
#Resultado: Accepted
#Data: 24/07/18 21:46:26
#Linguagem: Python 3
nInicial = int(input())
secNum = int(input())
while secNum <= nInicial:
    secNum = int(input())
contador = 0

while secNum > 0:
    secNum-= nInicial
    contador+= 1
    nInicial+=1

print(contador)