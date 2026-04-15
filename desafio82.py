lista=[]
listapar=[]
listaimpar=[]
verifica='S'
while verifica=='S':
    valor=int(input('Digite um valor: '))
    lista.append(valor)
    if valor%2==0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    verifica=input('Deseja continuar? [s/n]').upper().strip()[0]
print(f'A lista total ficou {lista}')
print(f'A de pares {listapar}')
print(f'A de valores ímpares {listaimpar}')