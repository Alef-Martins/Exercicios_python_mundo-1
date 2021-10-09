#Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 aumento de 10%, e para inferiores 15%.
salario = float(input('Informe o salário: '))
if salario > 1250:
    print(f'O valor do aumento será de: R${salario * 10 / 100:.2f} \n O salário final será de: R${salario + salario * 10 / 100:.2f}')
else:
    print(f'O valor do aumento será de: R${salario * 15 / 100:.2f} \nO salário final será de: R${salario + salario * 15 / 100:.2f}')
    