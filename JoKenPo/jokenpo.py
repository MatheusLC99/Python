""" Exercício inspirado no video Exercicio Python 45 - Game: Pedra Papel e Tesouro do canal Curso em Vídeo no youtube. """
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA'
[ 1 ] PAPEL
[ 2 ] TEESOURA''')
jogador = int(input('Qual é sua jogada ?\n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Máquina jogou {}'.format(itens[maquina]))
print('Sua escolha foi {}'.format(itens[jogador]))
print('-=' * 11)
if maquina == 0:  # Maquina escolheu PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif maquina == 1: # Maquina escolheu PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif maquina == 2: # Maquina escolheu TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')