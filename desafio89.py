print('-*'*18)
print(f'{"Boletim da turma":^30}')
print('-*'*18)
ficha=[]
resposta='S'
cont=0
while resposta=='S':
    nome=input('Nome: ')
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media=(n1+n2)/2
    ficha.append([nome, [n1, n2], media])
    resposta=input('Deseja continuar? [s/n] ').strip().upper()[0]
print('-='*18)
print(f'{"No.":<4}{"Nome:":<10}{"Média:":>8} ')
print('-='*18)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')

while True:
    print('-='*18)
    escolha=int(input('Gostaria de ver as notas de qual aluno? [-1 interrompe] '))
    if escolha==-1:
        print('Finalizando')
        break
    if escolha<=len(ficha):
        print(f'As notas do aluno {ficha[escolha][0]} foram {ficha[escolha][1]}')