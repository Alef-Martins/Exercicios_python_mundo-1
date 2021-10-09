#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas, Quantas letras ao todo (sem considerar os espaços), Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
new_var = len(nome.replace(' ', ''))
print(f'Seu nome tem ao todo {new_var} letras')
nome = nome.split()
primeiro_nome = nome[0]
print(f'Seu primeiro nome é {primeiro_nome}')
primeiro_nome = len(nome[0])
print(f'Seu primeiro nome tem {primeiro_nome} letras')
