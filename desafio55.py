print('leitura de pesos e classificação')
maior=0
menor=0
for c in range(1,6):
    peso=float(input('Peso da {}ª pessoa'.format(c)))
    if peso>maior:
        maior=peso
    if c==1:
        menor=peso
    elif peso<menor:
        menor=peso
print('O maior digitado foi {:.2f} e o menor foi {:.2f}'.format(maior,menor))