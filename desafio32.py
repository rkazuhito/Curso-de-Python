ano=int(input('Informe o ano a ser calculado: '))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))