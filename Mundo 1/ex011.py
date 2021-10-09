#Leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))
area = altura * largura
tinta = area / 2
print(f'A área total da parede é de {area}m² \n Será necessário {tinta} litros de tinta para pinta-la')