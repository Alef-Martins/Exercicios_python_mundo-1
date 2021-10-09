#Pega um número real digitado pelo usuário e mostra na tela sua porção inteira.
from math import trunc
num = float(input("Digite um número: "))
print(f"O número digitado foi: {num} e sua parte inteira é: {trunc(num)}")
print(f'Função int() número real: {num}, porção inteira: {int(num)}')