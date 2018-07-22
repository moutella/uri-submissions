#Nome: A Lenda de Flavious Josephus
#Resultado: Time limit exceeded
#Data: 22/07/18 15:42:50
#Linguagem: Python 3
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

import time
start = time.time()
nCasos = input()
casos = []
for x in range(0, int(nCasos)):
	casos.append(input().split())
	
for j in range(0, len(casos)):
	nPessoas = int(casos[j][0])
	nPulo = int(casos[j][1])
	pessoas = []
	for i in range(0, nPessoas):
		pessoas.append(i+1)
	indiceExiste = -1
	atual = 0
	contador = 0
	while len(pessoas)>1:
		contador+=1
		if (atual >= len(pessoas)):
			atual = 0
		if(contador == nPulo):
			del pessoas[atual]
			contador = 0
		else:
			atual+=1
	print("Case " +  str(j+1) + ":", pessoas[0])


