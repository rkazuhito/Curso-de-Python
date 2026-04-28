aluno={}
alunos=[]
resposta='S'
while resposta=='S':
    aluno['nome']=input('Nome: ')
    aluno['media']=float(input('Média: '))
    if aluno['media']>=7:
        aluno['situacao']='Aprovado'
    else:
        aluno['situacao']='Reprovado'
    alunos.append(aluno.copy())
    resposta=input('Deseja continuar? [S/N]').upper().strip()[0]
for c in range (0,len(alunos)):
    for k,v in alunos[c].items():
        print(f'{k}->{v}', end=' ')
    print()