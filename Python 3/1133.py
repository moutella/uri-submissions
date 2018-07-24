#Nome: Resto da Divisão
#Resultado: Wrong answer (10%)
#Data: 24/07/18 20:36:47
#Linguagem: Python 3
A = int(input())
B = int(input())
soma = 0
if(A>B):
    A ^= B
    B ^= A
    A ^= B
for i in range(A,B):
    resto = i%5
    if resto == 2 or resto == 3:
        print(i)