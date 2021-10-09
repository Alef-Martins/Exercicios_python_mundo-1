#Faça um programa que leia um frase pelo teclado e mostre quantas vezes aparece a letra 'a', emque posição ela aparece pela primeira vez e na última
frase = str(input('Digite um frase: ')).upper().strip()
print('A letra A aparece {} vezes na fraze' .format(frase.count('A')))
print('Aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('E pela última vez na posição: {}' .format(frase.rfind('A')+1))