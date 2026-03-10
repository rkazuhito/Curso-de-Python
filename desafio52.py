print('Desafio dos números primos')
div=0
n=int(input('Digite um número: '))
for c in range(n,0,-1):
    if n%c==0:
        print('\033[31m{}\033[m'.format(c), end=' ')
        div+=1
    else:
        print('\033[32m{}\033[m'.format(c), end=' ')
if div==2:
    print('\nPrimo')
else:
    print('\nNão primo')