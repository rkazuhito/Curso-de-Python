import random
from time import sleep
from operator import itemgetter
jogadas={}
ranking={}
for c in range(1,5):
    jogadas[c]=random.randint(1,6)
print('Valores Sorteados: ')
sleep(1)
print('...')
sleep(0.5)
print('..')
sleep(0.5)
print('.')
sleep(0.5)
for k, v in jogadas.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1.5)
ranking=sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-='*25)
for k,v in enumerate(ranking):
    print(f'O jogador {v[0]} ficou em {k+1}º tirando o valor {v[1]} no dado')
    sleep(1)