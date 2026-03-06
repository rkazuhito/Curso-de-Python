import datetime
anoatual=datetime.date.today().year
anonasc=int(input('Qual o ano de nascimento? '))
idade=anoatual-anonasc
if idade<18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
elif idade==18:
    print('Você esta no ano de se alistar')
else:
    print('Ja se passaram {} anos da sua idade de se alistar'.format(idade-18))