#Nome: A Lenda de Flavious Josephus
#Resultado: Time limit exceeded
#Data: 22/07/18 02:39:34
#Linguagem: Python 3
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
nCasos = input()
for x in range(0, int(nCasos)):
	casoAtual = input().split()
	nPessoas = int(casoAtual[0])
	nPulo = int(casoAtual[1])
	pessoas = []
	pessoasBack = []
	for i in range(0, nPessoas):
		pessoas.append(i+1)
		pessoasBack.append(i+1)
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
	print("Case " +  str(x) + ":", pessoasBack.index(pessoas[0])+1)