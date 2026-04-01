print('\033[1;33;44m   CADASTRO DE PRODUTOS   \033[m')
tot=maismil=menor=cont=0
while True:
    print('-'*20)
    nome=input('Nome do produto: ')
    preco=float(input('Preço: R$'))
    cont+=1
    tot+=preco
    if cont==1:
        menor=preco
        nomemenor=nome
    else:
        if preco<menor:
            menor=preco
            nomemenor=nome
    if preco>1000:
        maismil+=1
    escolha=input('Deseja cadastrar mais um produto? [S/N]').strip().upper()[:1]
    if escolha=='N':
        break
print(f'Ao todo foram cadastrados {cont} produtos e o somatório do valor foi de R${tot:.2f}. \n Temos {maismil} produto(s) custando mais de mil reais. \n O produto mais barato foi {nomemenor} custando R${menor:.2f}')