print('=-'*15)
print('\033[1;31;43mCálculo de empréstimo bancário\033[m')
print('=-'*15)
casa=float(input('Qual o valor da casa? R$ '))
sal=float(input('Qual o seu salário? R$'))
anos=int(input('Em quantos anos será pago? '))
prest=casa/(anos*12)
if prest>=sal*0.3:
    print('empréstimo negado')
else:
    print('empréstimo aprovado com prestações no valor de R${:.2f}'.format(prest))