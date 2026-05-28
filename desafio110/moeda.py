def aumentar(val=0, porcent=0, formato=False):
    res=val+val*porcent/100
    return res if formato is False else moeda(res)

def diminuir(val=0,porcent=0, formato=False):
    res=val-val*porcent/100
    return res if formato is False else moeda(res)

def dobro(val=0, formato=False):
    res=val*2
    return res if formato is False else moeda(res)

def metade(val=0, formato=False):
    res=val/2
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0,taxaa=10,taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco,taxar,True)}')
    print('-'*40)
