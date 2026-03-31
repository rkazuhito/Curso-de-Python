import random
print('\033[1;33;44m   JOGO PAR OU ÍMPAR   \033[m')
n=int(input('Escolha um número de 1 a 10: '))
escolha=input('Escolha par ou ímpar [P/I]: ').strip().upper()
npc=random.randint(1,10)
vitoria=0
while True:
    if escolha=='P':
        if (n+npc)%2==0:
            vitoria+=1
            print('{} + {} = {} que é par, você ganhou'.format(n,npc,n+npc))
        else:
            print('{} + {} = {} que é ímpar, você perdeu'.format(n,npc,n+npc))
            break
    elif escolha=='I':
        if (n+npc)%2!=0:
            vitoria+=1
            print('{} + {} = {} que é ímpar, você ganhou'.format(n,npc,n+npc))
        else:
            print('{} + {} = {} que é par, você perdeu'.format(n,npc,n+npc))
            break
    n=int(input('Escolha um número de 1 a 10: '))
    escolha=input('Escolha par ou ímpar [P/I]: ').strip().upper()
    npc=random.randint(1,10)
print('Fim de jogo, ao total foram {} vitórias, parabéns!!!'.format(vitoria))