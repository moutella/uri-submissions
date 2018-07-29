#Nome: Tri
#Resultado: Accepted
#Data: 29/07/18 19:44:55
#Linguagem: Python 3
valores = input().split()
a = int(valores[0])
b = int(valores[1])
if a == b:
    print(a)
else:
    print(max(a, b))
