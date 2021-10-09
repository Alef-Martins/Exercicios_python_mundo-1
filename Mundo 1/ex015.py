#Calcula o valor do aluguel de um carro, sendo 60R$/Dia e 0,15R$/Km
dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km rodados: '))
preco = dias * 60 + km * 0.15
print(f'O valor do aluguel será de: R${preco:.2f}')