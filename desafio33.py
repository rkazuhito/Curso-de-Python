n1=int(input('Digite um número: '))
n2=int(input('Mais um: '))
n3=int(input('O último: '))
if n1>n2:
    maior=n1
    if n3>n1:
        maior=n3
else:
    maior=n2
    if n3>n2:
        maior=n3

if n1<n2:
    menor=n1
    if n3<n1:
        menor=n3
else:
    menor=n2
    if n3<n2:
        menor=n3
print('Menor = {} \nMaior = {}'.format(menor,maior))