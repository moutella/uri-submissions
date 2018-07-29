#Nome: Bem
#Resultado: Accepted
#Data: 29/07/18 19:00:08
#Linguagem: Python 3
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if(b-a < c-b):
    print(":)")
elif(c > b and b-a == c-b):
    print(":)")
else:
    print(":(")