# Essa função tem como objetivo encontrar os valores para os 
# catetos e a hipotenusa de um triângulo retângulo 
# utilizando o Teorema de Pitágoras h²= a² + b²

import math

def pitagoras(h, a, b):
    if h == 0 and a != 0 and b != 0:
        h = math.sqrt((a**2)+(b**2))
        result = h
    elif a == 0 and h != 0 and b != 0:
        a = math.sqrt((h**2)-(b**2))
        result = a
    elif b == 0 and a != 0 and h!= 0:
        b = math.sqrt((h**2)-(a**2))
        result = b
    return result 

# variable = (pitagoras(0,4,3))
# print(f"O valor desconhecido no seu triângulo retângulo é {variable}")
