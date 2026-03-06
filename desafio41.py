import datetime
print('--'*35)
anoatual=datetime.date.today().year
print('  Programa para atletas da Confederação Nacional de Natação {}'.format(anoatual))
print('--'*35)
anonasc=int(input('Informe o ano de nascimento do atleta: '))
idade=anoatual-anonasc
if idade<=9:
    print('Mirim')
elif idade<=14:
    print('Infantil')
elif idade<=19:
    print('Junior')
elif idade<=25:
    print('Sênior')
else:
    print('Master')