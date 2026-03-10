import time
print('-'*12)
print('Soma somente dos pares!')
print('-'*12)
soma=0
for c in range(0,6):
    n=int(input('Digite um número: '))
    if n%2==0:
        soma=soma+n
print('Calculando', end=' ')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('A soma dos pares digitados ficou em {}'.format(soma))