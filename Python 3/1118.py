#Nome: Várias Notas Com Validação
#Resultado: Wrong answer (80%)
#Data: 24/07/18 20:21:33
#Linguagem: Python 3
novoCalc = 1
while(novoCalc):
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
    print("novo calculo (1-sim 2-nao")
    novoCalc = int(input())
    print(novoCalc)
    while(novoCalc!= 1 and novoCalc != 2):
        print("novo calculo (1-sim 2-nao")
        novoCalc = int(input())
        print (novoCalc)
    if (novoCalc == 2):
        novoCalc = 0