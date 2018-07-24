#Nome: Idades
#Resultado: Accepted
#Data: 24/07/18 21:40:29
#Linguagem: Python 3
soma = 0
contador = 0
while 1:
    valor = int(input())
    if(valor<0):
        print("{:.2f}".format(soma/contador))
        break
    soma += valor
    contador+=1
