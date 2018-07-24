#Nome: Múltiplos de 13
#Resultado: Wrong answer (100%)
#Data: 24/07/18 20:33:22
#Linguagem: Python 3
A = int(input())
B = int(input())
soma = 0
for i in range(A,B+1):
    if i % 13:
        soma+=i
print(soma)
