import datetime
anoat=datetime.date.today().year
maior=0
menor=0
print('= ='*12)
print('Análise da idade das 7 pessoas em {}'.format(anoat))
print('= ='*12)
for c in range(1,8):
    ano=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if anoat-ano>=18:
        maior+=1
    else:
        menor+=1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores'.format(maior,menor))