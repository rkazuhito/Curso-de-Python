import random
import time
print('#'*28)
print('\033[1;46mJogue JOKENPO com a máquina\033[m\n\033[1;46mVocê acha que pode vencer? \033[m')
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
print('#'*28)
jogador=int(input('Qual a sua jogada?'))
maquina=random.randint(0,2)
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
print('#'*28)
if jogador==0:
    if maquina==0:
        print('Você jogou PEDRA e a máquina PEDRA, EMPATE')
    elif maquina==1:
        print('Você jogou PEDRA e a máquina PAPEL, DERROTA')
    else:
        print('Você jogou PEDRA e a máquina TESOURA, VITÓRIA')
elif jogador==1:
    if maquina==0:
        print('Você jogou PAPEL e a máquina PEDRA, VITÓRIA')
    elif maquina==1:
        print('Você jogou PAPEL e a máquina PAPEL, EMPATE')
    else:
        print('Você jogou PAPEL e a máquina TESOURA, DERROTA')
elif jogador==2:
    if maquina==0:
        print('Você jogou TESOURA e a máquina PEDRA, DERROTA')
    elif maquina==1:
        print('Você jogou TESOURA e a máquina PAPEL, VITÓRIA')
    else:
        print('Você jogou TESOURA e a máquina TESOURA, EMPATE')
else:
    print('Jogada inválida, por favor selecione um número do menu 0,1 ou 2')