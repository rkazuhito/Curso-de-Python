def aumentar(val=0, porcent=0):
    return val+val*porcent/100

def diminuir(val=0,porcent=0):
    return val-val*porcent/100

def dobro(val=0):
    return val*2

def metade(val=0):
    return val/2

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')