#Programa que leia o comprimento dos catetos (opsto e adjacente) de um triângulo retângulo
#Calcule e mostre a hipotenusa
from math import hypot
adjacente = float(input('Comprimento do cateto adjacente: '))
oposto = float(input('Comprimento do cateto oposto: '))
hipotenusa = hypot(adjacente , oposto)
print(f'A hipotenusa vale: {hipotenusa:.2f}')
