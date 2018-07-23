#Nome: Salário com Bônus
#Resultado: Accepted
#Data: 23/07/18 17:11:08
#Linguagem: Python 3
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

nome = input()
sal = input()
vendas = input()

total = float(sal) + float(vendas)*0.15

print("TOTAL = R$ {:.2f}".format(total))