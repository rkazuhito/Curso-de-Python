resposta='S'
lista=[]
while resposta=='S':
    num=input('Digite um valor para ser adicionado à lista: ')
    if num not in lista:
        lista.append(num)
    resposta=input('Deseja continuar? (S/N)').strip().upper()[0]
lista.sort()
print(lista)
