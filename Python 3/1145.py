#Nome: Sequência Lógica 2
#Resultado: Accepted
#Data: 24/07/18 20:59:10
#Linguagem: Python 3
entradas = input()
entrada = entradas.split()
A = int(entrada[0])
B = int(entrada[1])

for i in range(1, B+1):
    if(i%A):
        print(i, end = " ")
    if not i % A:
        print(i, end="")
        print()