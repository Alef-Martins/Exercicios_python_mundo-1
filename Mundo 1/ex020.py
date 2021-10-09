#leia quatro nomes em variáveis e mostre uma ordem aleatória
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos será:')
print(lista)
