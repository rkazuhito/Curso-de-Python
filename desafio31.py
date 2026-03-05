x=float(input('Informe a distância da viagem em Km: '))
preco=0
if x>200:
    preco=x*0.45
else:
    preco=x*0.5
print('A sua viagem de {:.2f}Km terá um custo de R${:.2f}'.format(x,preco))