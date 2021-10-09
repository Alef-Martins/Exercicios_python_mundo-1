#Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print('As retas PODEM formar um triângulo')
else:
    print('As retas NÃO PODEM formar um triângulo')
    