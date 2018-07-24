#Nome: Idades
#Resultado: Wrong answer (100%)
#Data: 24/07/18 21:39:44
#Linguagem: Python 3
soma = 0
contador = 0
while 1:
    valor = int(input())
    if(valor<0):
        print(soma/contador)
        break
    soma += valor
    contador+=1
