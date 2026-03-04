import random
import time
print('Esse é o jogo da advinhação... Vou pensar em um número de 1 a 5 e você tenta advinhar')
retry=1
n=int(input('Tente advinhar: '))
npc=random.randint(1,5)
print('E lá vamos nós...')
time.sleep(2)
if n==npc:
    print('Parabéns vc acertou!!!')
else:
    print('Você escolheu {} e eu escolhi {}, você errou....'.format(n,npc))