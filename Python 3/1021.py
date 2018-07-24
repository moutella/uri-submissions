#Nome: Notas e Moedas
#Resultado: Wrong answer (10%)
#Data: 24/07/18 16:52:06
#Linguagem: Python 3
valor = float(input())
nota100 = valor//100
valor %= 100
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor //10
valor %= 10
nota5 = valor // 5
valor %= 5
nota2 = valor //2
valor %= 2
moeda100 = valor //1
valor %= 1
moeda50 = valor //0.5
valor %= 0.5
moeda25 = valor // 0.25
valor %= 0.25
moeda10 = valor//0.1
valor %= 0.1
moeda5 =valor //0.05
valor %= 0.05
moeda1 = valor //0.01
moeda1+=1
valor %= 0.01
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(nota100)))
print("{} nota(s) de R$ 50.00".format(int(nota50)))
print("{} nota(s) de R$ 20.00".format(int(nota20)))
print("{} nota(s) de R$ 10.00".format(int(nota10)))
print("{} nota(s) de R$ 5.00".format(int(nota5)))
print("{} nota(s) de R$ 2.00".format(int(nota2)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moeda100)))
print("{} moeda(s) de R$ 0.50".format(int(moeda50)))
print("{} moeda(s) de R$ 0.25".format(int(moeda25)))
print("{} moeda(s) de R$ 0.10".format(int(moeda10)))
print("{} moeda(s) de R$ 0.05".format(int(moeda5)))
print("{} moeda(s) de R$ 0.01".format(int(moeda1)))
