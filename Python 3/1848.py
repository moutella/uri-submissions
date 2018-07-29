#Nome: Corvo Contador
#Resultado: Wrong answer (50%)
#Data: 29/07/18 19:06:35
#Linguagem: Python 3
count = 0
soma = 0
while count < 3:
    momento = input()
    if momento == "caw caw":
        count+=1
        print(soma)
        soma = 0
    else:
        x = 2 - momento.index("*")
        soma += 2 ** x
