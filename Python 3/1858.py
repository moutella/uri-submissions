#Nome: A Resposta de Theon
#Resultado: Accepted
#Data: 29/07/18 19:17:38
#Linguagem: Python 3
nVal = int(input())
valStr = input().split()
valores =[]
for str in valStr:
    valores.append(int(str))
print(valores.index(min(valores))+1)