#Nome: Múltiplos de 13
#Resultado: Accepted
#Data: 24/07/18 20:34:36
#Linguagem: Python 3
A = int(input())
B = int(input())
soma = 0
if(A>B):
    A ^= B
    B ^= A
    A ^= B
for i in range(A,B+1):
    if i % 13:
        soma+=i
print(soma)