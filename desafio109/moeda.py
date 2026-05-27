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