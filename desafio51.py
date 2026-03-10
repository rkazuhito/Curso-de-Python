print('Cálculo dos 10 primeiros termos de uma PA')
a=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
for c in range(0,10):
    print(a+r*c, end=' -> ')
print('ACABOU')