#Nome: O Filme
#Resultado: Runtime error
#Data: 29/07/18 21:42:02
#Linguagem: Python 3
entradas = input().split()

dif = int(entradas[1]) - int(entradas[0])

percent = dif / int(entradas[0])
percent *= 100
print("{:.2f}%".format(percent))