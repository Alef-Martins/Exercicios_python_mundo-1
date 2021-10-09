#Escreva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Distância da viagem: '))
preço = 0
if distancia > 200:
    preço = distancia * 0.45
    print(f'O valor da passagem será de R${preço:.2f}')
else:
    preço = distancia * 0.50
    print(f'O valor da passagem será de R${preço:.2f}')
