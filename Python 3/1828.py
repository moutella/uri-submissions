#Nome: Bazinga!
#Resultado: Presentation error
#Data: 29/07/18 17:46:20
#Linguagem: Python 3
nVal = int(input())
for i in range(nVal):
    palavras = input().split()
    possiveis = ["pedra", "lagarto", "Spock", "tesoura", "papel"]
    diferenca = possiveis.index(palavras[1]) - possiveis.index(palavras[0])
    if(diferenca < 0):
        diferenca+=5
    if(diferenca == 1 or diferenca == 3):
        print("Caso #{}: Bazinga!".format(i+1))
    elif(diferenca ==0):
        print("Caso #{}: De novo!".format(i+1))
    else:
        print("Caso #{}:Raj trapaceou!".format(i+1))