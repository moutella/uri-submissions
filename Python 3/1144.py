#Nome: Sequência Lógica
#Resultado: Accepted
#Data: 24/07/18 20:44:48
#Linguagem: Python 3
num = int(input())
for i in range(1, num+1):
    print("{} {} {}".format(i, i*i, i*i*i))
    print("{} {} {}".format(i, i * i + 1, i * i * i + 1))