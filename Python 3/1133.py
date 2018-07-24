#Nome: Resto da Divisão
#Resultado: Accepted
#Data: 24/07/18 20:37:03
#Linguagem: Python 3
A = int(input())
B = int(input())
soma = 0
if(A>B):
    A ^= B
    B ^= A
    A ^= B
for i in range(A+1,B):
    resto = i%5
    if resto == 2 or resto == 3:
        print(i)