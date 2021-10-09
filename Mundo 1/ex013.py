#Leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Informe o salário atual: '))
print(f'O novo salário com 15% de aumento será de: R${salario + (salario * 15 / 100)}')