#Nome: Seis Números Ímpares
#Resultado: Accepted
#Data: 24/07/18 18:53:10
#Linguagem: Python 3
num = int(input())
if not num%2:
    num+=1
for i in range(0,6):
    print(num + i*2)