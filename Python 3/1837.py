#Nome: Prefácio
#Resultado: Accepted
#Data: 29/07/18 18:37:34
#Linguagem: Python 3
valores = input().split()
b = int(valores[0])%int(valores[1])
a = int(valores[0])//int(valores[1])
if(b<0):
    a+=1
    b+=abs(int(valores[1]))
print(a, b)