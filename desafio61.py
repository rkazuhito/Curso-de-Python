print('\033[1;33;44m   10 PRIMEIROS TERMOS DE UMA PA   \033[m')
n=int(input('Informe o valor inicial: '))
r=int(input('Informe a razão da PA: '))
for c in range(0,10):
    print('{} ->'.format(n+r*c), end=' ')
print('FIM')