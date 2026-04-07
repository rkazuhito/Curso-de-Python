n1=int(input('Digite um valor: '))
n2=int(input('Digite um valor: '))
n3=int(input('Digite um valor: '))
n4=int(input('Digite um valor: '))
tupla=(n1,n2,n3,n4)
cont9=contpar=0
print(tupla)
print('-='*20)
print('Os números pares digitados foram:', end=' ')
for c in range(0,len(tupla)):
    if tupla[c]==9:
        cont9+=1
    if tupla[c]%2==0:
        print(f'{tupla[c]}', end=' ')
        contpar+=1
if contpar==0:
    print('Nenhum', end=' ')
if 3 in tupla:
    print(f'\nO primeiro 3 foi digitado na posição {tupla.index(3)+1}')
else:
    print('\nNão foi digitado nenhum 3')
print(f'O valor 9 apareceu {cont9} vezes')