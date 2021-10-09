#Program que leia um número entre 0 e 9999 e mostre quantas unidades, dezenas, centenas e milhares existem
numero = input('Digite um núero entre 0 e 9999: ')
if len(numero) == 4:
    print(f'Analizando o número {numero}')
    print(f'unidade: {numero[0]}')
    print(f'dezena: {numero[1]}')
    print(f'centena: {numero[2]}')
    print(f'milhar: {numero[3]}')
elif len(numero) == 3:
    print(f'Analizando o número {numero}')
    print(f'Unidade: {numero[0]}')
    print(f'Dezena: {numero[1]}')
    print(f'Centena: {numero[2]}')
    print(f'Milhar: 0')
elif len(numero) == 2:
    print(f'Analizando o número {numero}')
    print(f'Unidade: {numero[0]}')
    print(f'Dezena: {numero[1]}')
    print('Centena: 0')
    print('Milhar: 0')
elif len(numero) == 1:
    print(f'Analizando o número {numero}')
    print(f'Unidade: {numero[0]}')
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')
else:
    print('Nenhum número foi informado!')
