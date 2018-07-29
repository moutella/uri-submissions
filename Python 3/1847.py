#Nome: Bem
#Resultado: Wrong answer (20%)
#Data: 29/07/18 18:52:36
#Linguagem: Python 3
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if(b-a <= c-b):
    print(":)")
else:
    print(":(")