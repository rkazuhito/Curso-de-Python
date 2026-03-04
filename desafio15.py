x=float(input('Qual a distância em Km percorrida? '))
t=int(input('Por quantos dias foi alugado? '))
preco=t*60+0.15*x
print('Você deve R${:.2f}'.format(preco))
