pessoa={}
pessoas=[]
continuar='S'
totidade=0
mulheres=[]
while continuar=='S':
    pessoa['nome']=input('Nome: ')
    sexo=input('Sexo (M/F): ').strip().upper()[0]
    while sexo !='M' and sexo!='F':
        print(f'Você digitou {sexo}, precisa ser M ou F')
        sexo=input('Sexo (M/F): ').strip().upper()[0]
    pessoa['sexo']=sexo
    if sexo=='F':
        mulheres.append(pessoa['nome'])
    pessoa['idade']=int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continuar=input('Deseja continuar? (S/N)').strip().upper()[0]
    while continuar!='S' and continuar!='N':
        print(f'Você digitou {continuar}, precisa ser S ou N')
        continuar=input('Deseja continuar? (S/N)').strip().upper()[0]
print('-='*20)
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas')
for c in range(0,len(pessoas)):
    totidade+=pessoas[c]['idade']
media=totidade/len(pessoas)
print(f'A média de idades ficou em: {media:.2f}')
if len(mulheres) == 0:
    print('Não há mulheres cadastradas.')
else:
    print('As mulheres cadastradas foram: ', end='')
    for c in range(0, len(mulheres)):
        print(mulheres[c], end=' / ')
print()
print('As pessoas que têm idade acima da média são:')
for c in range(0,len(pessoas)):
    if pessoas[c]['idade']>media:
        print(f'{pessoas[c]["nome"]} - {pessoas[c]["idade"]} anos')