#Nome: Soma de Ímpares Consecutivos III
#Resultado: Accepted
#Data: 24/07/18 21:58:36
#Linguagem: Python 3
nTestes = int(input())
for i in range(0,nTestes):
    teste = input().split()
    A = int(teste[0])
    B = int(teste[1])
    soma = 0
    if(not A%2):
        A+=1
    for j in range(0, B):
        soma += A + j*2
    print(soma)