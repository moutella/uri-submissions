#Nome: De Quem é a Vez?
#Resultado: Accepted
#Data: 29/07/18 19:20:32
#Linguagem: Python 3
nCasos = int(input())
for i in range(nCasos):
    parImp = input().split()
    valores = input().split()
    if not (int(valores[0]) + int(valores[1]))%2:
        print(parImp[parImp.index("PAR")-1])
    else:
        print(parImp[parImp.index("IMPAR") - 1])