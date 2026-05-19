from random import randint
numeros=[]
def sorteia(lista):
    c=0
    while c<5:
        lista.append(randint(0,10))
        c+=1
def somaPar(numeros):
    soma=0
    for c in range(0,len(numeros)):
        if numeros[c]%2==0:
            soma+=numeros[c]
    print(f'A soma dos pares dessa lista é igual a {soma}')
sorteia(numeros)
print(f'A lista de números aleatórios gerados pela função foi {numeros}')
somaPar(numeros)