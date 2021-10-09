#Leia um êngulo qualquer e mostrwe na tel o seno, coseno e tangente do mesmo.
from math import sin, cos, tan, radians
ang = int(input('Informe um ângulo : '))
print(f'O seno de {ang} é: {sin(radians(ang)):.2f}')
print(f'O coseno de {ang} é: {cos(radians(ang)):.2f}')
print(f'A tangente de {ang} é: {tan(radians(ang)):.2f}')
