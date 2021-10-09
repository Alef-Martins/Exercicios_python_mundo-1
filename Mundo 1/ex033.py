#Crie um programa que leia e números e mostre qual é o maior e o menor.
num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
num3 = int(input('Informe o 3º número: '))
if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior')
    if num2 < num3:
        print(f'O número {num2} é o menor')
    elif num3 < num2:
        print(f'O número {num3} é o menor')
elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior')
    if num1 < num3:
        print(f'O número {num1} é o menor')
    elif num3 < num1:
        print(f'O número {num3} é o menor')
elif num3 > num1 and num3 > num2:
    print(f'O número {num3} é o maior')
    if num1 < num2:
        print(f'O número {num1} é o menor')
    elif num2 < num1:
        print(f'O número {num2} é o menor')
