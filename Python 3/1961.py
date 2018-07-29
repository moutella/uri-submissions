#Nome: Pula Sapo
#Resultado: Accepted
#Data: 29/07/18 21:25:44
#Linguagem: Python 3
valores = input().split()
canos = input().split()
for x in range(int(valores[1])-1):
    if abs(int(canos[x]) - int(canos[x + 1])) > int(valores[0]):
        print("GAME OVER")
        exit()

print("YOU WIN")
