#Nome: Bem
#Resultado: Wrong answer (10%)
#Data: 29/07/18 18:44:44
#Linguagem: Python 3
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if(c-b > b-a):
    print(":)")
else:
    print(":(")