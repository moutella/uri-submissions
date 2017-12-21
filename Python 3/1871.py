#Nome: Zero vale Zero
#Resultado: Accepted
#Data: 21/12/17 15:10:06
#Linguagem: Python 3
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

import sys
while 1:
    n, x = input().split()
    if n == x == "0":
        sys.exit()
    res = int(n) + int(x)
    strings = str(res).split("0", -1)
    f = ""
    for i in range(0, strings.__len__()):
        f += strings[i]
    print(f)
