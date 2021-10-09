#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa custa R$7,00 por cada Km acima do limite
velocidade = int(input('Velocidade do veículo: '))
multa = 0
if velocidade > 80:
    multa = 7.00 * (velocidade - 80)
    print(f'Vecê foi multado em R${multa:.2f}')
else:
    print('Velocidade compatível com a via')

