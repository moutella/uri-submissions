#Nome: Soma de Pares Consecutivos
#Resultado: Accepted
#Data: 24/07/18 22:01:34
#Linguagem: Python 3
while 1:
    teste = int(input())
    if(teste == 0):
        break
    soma = 0
    if(teste%2):
        teste+=1
    for j in range(0, 5):
        soma += teste + j*2
    print(soma)