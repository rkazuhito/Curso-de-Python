cadastro={}
from datetime import datetime
print('Cadastro de Carteira de Trabalho')
print('-='*5)
cadastro['nome']=input('Nome: ')
cadastro['anonascimento']=int(input('Ano de nascimento: '))
cadastro['carteira']=int(input('Carteira de trabalho (0 não tem): '))
if cadastro['carteira']!=0:
    cadastro['contratação']=int(input('Ano de contratação: '))
    cadastro['salario']=float(input('Salário: '))
    cadastro['aposentadoria']=(datetime.now().year-cadastro['anonascimento'])+(cadastro['contratação'] + 35)-datetime.now().year
print('-='*5)  
for k,v in cadastro.items():
    print(f'O {k} tem valor {v}')