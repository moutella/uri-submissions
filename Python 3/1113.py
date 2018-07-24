#Nome: Crescente e Decrescente
#Resultado: Accepted
#Data: 24/07/18 20:03:16
#Linguagem: Python 3
while 1:
    valores = input().split()
    A = int(valores[0])
    B = int(valores[1])
    if(A==B):
        break
    if(A>B):
        print("Decrescente")
    else:
        print("Crescente")
