#crie um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep #FAZ O COMPUTADOR PARAR POR ALGUNS SEGUNDOS
num = randint(0, 5)
resp = int(input('Adivinhe o número entre 0 e 5: '))
print('...PROCESSANDO...')
sleep(2) #Parada!
if resp == num:
    print(f'Você digitou {resp}, parabéns, vocễ acertou')
else:
    print(f'Você digitou {resp}, você errou, o número é {num}')