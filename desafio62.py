print('\033[1;33;44m   PA APRIMORADA   \033[m')
n=int(input('Primeiro termo: '))
r=int(input('razão da PA: '))
for x in range(0,10):
    print('{} ->'.format(n+r*x), end=' ')
tot=10
c=1
while c>0:
    c=int(input('\n Quantos mais termos você gostaria de ver? '))
    for x in range(tot,tot+c):
        print('{} ->'.format(n+r*x), end=' ')
    tot=tot+c