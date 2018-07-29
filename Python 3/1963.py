#Nome: O Filme
#Resultado: Accepted
#Data: 29/07/18 21:42:36
#Linguagem: Python 3
entradas = input().split()

dif = float(entradas[1]) - float(entradas[0])

percent = dif / float(entradas[0])
percent *= 100
print("{:.2f}%".format(percent))