import time
import random
print('Sou seu computador...')
time.sleep(1)
print('Vamos jogar um jogo!!')
time.sleep(1)
print('Vou pensar em um número entre 1 e 10 e você tenta adivinhar...')
time.sleep(1)
print('...')
time.sleep(0.5)
print('..')
time.sleep(0.5)
print('.')
npc=random.randint(1,10)
print('Pensei...')
n=int(input('Qual o seu palpite? '))
cont=1
while npc!=n:
    n=int(input('Errou, tente outra vez '.format(npc)))
    cont+=1
print('PARABÉNS!!! Eu pensei no {}'.format(npc))
print('Você acertou em {} tentativas'.format(cont))