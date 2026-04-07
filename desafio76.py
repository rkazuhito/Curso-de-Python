listagem=('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo',25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila',120.32,
          'Canetas',22.30,
          'Livro',34.90)
print('\033[1;;44m-\033[m'*40)
print(f'{"Listagem de Preços":^40}')
print('\033[1;;44m-\033[m'*40)
for item in range(0,len(listagem)):
    if item%2==0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-'*40)