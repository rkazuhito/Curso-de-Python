lista=[]
maior=menor=posmen=posmai=0
for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
    if c==0:
        menor=lista[c]
    else:
        if lista[c]<menor:
            menor=lista[c]
    if lista[c]>maior:
        maior=lista[c]
print(f'A lista digitada ficou assim: {lista}')
print(f'O maior valor digitado foi o {maior} na(s) posição(ões) ->', end=' ')
for indice, valor in enumerate(lista):
    if maior==valor:
        print(f'{indice}', end=' ')
print(f'\nO menor valor digitado foi o {menor} na(s) posição(ões) ->', end=' ')
for indice,valor in enumerate(lista):
    if menor==valor:
        print(f'{indice}', end=' ')