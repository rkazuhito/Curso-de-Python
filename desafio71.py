print('\033[1;33;44m   CAIXA ELETRÔNICO   \033[m')
valor=int(input('Qual valor gostaria de sacar? R$ '))
notacem=notacinquenta=notavinte=notadez=notaum=0
while valor>0:
    if valor>=100:
        while valor>=100:
            valor-=100
            notacem+=1
    elif valor>=50:
        while valor>=50:
            valor-=50
            notacinquenta+=1
    elif valor>=20:
        while valor>=20:
            valor-=20
            notavinte+=1
    elif valor>=10:
        while valor>=10:
            valor-=10
            notadez+=1
    elif valor>=1:
        while valor>=1:
            valor-=1
            notaum+=1
print('Com esse valor você irá sacar: ')
print(f'{notacem} notas de 100')
print(f'{notacinquenta} notas de 50')
print(f'{notavinte} notas de 20')
print(f'{notadez} notas de 10')
print(f'{notaum} notas de 1')