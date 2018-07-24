#Nome: Positivos e Média
#Resultado: Accepted
#Data: 24/07/18 18:49:57
#Linguagem: Python 3
valores = []
nPos = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        nPos+=1
        valores.append(x)
print("{} valores positivos".format(nPos))
media = 0
for i in range(0, nPos):
    media += valores[i]
media = media/nPos
print("{:.1f}".format(media))
