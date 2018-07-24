#Nome: Somando Inteiros Consecutivos
#Resultado: Accepted
#Data: 24/07/18 21:27:09
#Linguagem: Python 3
valores = input().split()
A = int(valores[0])
B = int(valores[-1])
total = 0
for i in range(0, B):
    total+=(A+i)
print(total)