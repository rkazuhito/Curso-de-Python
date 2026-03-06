print('- -'*10)
print('\033[1;46m         LOJAS BRASIL         \033[m')
print('- -'*10)
preco=float(input('Preço R$:'))
print('''FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão
''')
escolha=int(input('Escolha: '))
if escolha==1:
    preco=preco*0.9
elif escolha==2:
    preco=preco*0.95
elif escolha==3:
    preco=preco
else:
    preco=preco*1.2
print('O preço final ficou em R${:.2f}'.format(preco))