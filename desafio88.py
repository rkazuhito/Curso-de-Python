from random import randint
print('*-'*30)
print('          Jogo da MEGA       ')
print('*-'*30)
qtd = int(input('Quantos sorteios você gostaria de ver? '))
jogo = []
for i in range(qtd):
    lista = []
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogo.append(lista[:])
    print(f'Jogo {i+1}: {lista}')