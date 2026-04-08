lista=[]
maior=0
posmen=[]
posmai=[]
for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
    if c==0:
        menor=lista[c]
        posmen.append(c)
    else:
        if lista[c]<menor:
            menor=lista[c]
            posmen.append(c)
    if lista[c]>maior:
        maior=lista[c]
        posmai.append(c)
print(f'A lista digitada ficou assim: {lista}')
print(f'O maior valor digitado foi o {maior} na posição {posmai}')
print(f'O menor valor digitado foi o {menor} na posição {posmen}')