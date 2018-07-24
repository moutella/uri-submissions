#Nome: Sequência Lógica 2
#Resultado: Presentation error
#Data: 24/07/18 20:54:53
#Linguagem: Python 3
entradas = input()
entrada = entradas.split()
A = int(entrada[0])
B = int(entrada[1])

for i in range(1, B):
    print(i,"", end = "")
    if not i % A:
        print()
print(B, end="")