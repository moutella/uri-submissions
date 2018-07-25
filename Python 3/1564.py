#Nome: Vai Ter Copa?
#Resultado: Accepted
#Data: 25/07/18 22:11:27
#Linguagem: Python 3
while 1:
    try:
        entrada = int(input())
        if entrada > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break