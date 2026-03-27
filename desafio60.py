print('\033[1;33;44m   CALCULANDO O FATORIAL   \033[m')
n=int(input('Informe o valor: '))
fat=1
while n>1:
    print('{} x'.format(n),end=' ')
    fat=fat*n
    n-=1
print(' 1 = {}'.format(fat))