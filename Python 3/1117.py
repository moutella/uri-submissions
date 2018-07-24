#Nome: Validação de Nota
#Resultado: Accepted
#Data: 24/07/18 20:13:18
#Linguagem: Python 3
nota = -1
nota2 = -1
notaval = 0
while not notaval:
    nota = float(input())
    notaval = 1
    if(nota < 0 or nota > 10):
        print("nota invalida")
        notaval = 0
notaval = 0
while not notaval:
    nota2 = float(input())
    notaval = 1
    if (nota2 < 0 or nota2 > 10):
        print("nota invalida")
        notaval = 0
    else:
        print("media = {:.2f}".format((nota+nota2)/2))
        break

