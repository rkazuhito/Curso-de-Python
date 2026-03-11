print('-_'*10)
print('Analisador de grupo')
print('-_'*10)
soma=0
velho=0
contf=0
for c in range(1,5):
    print('-_'*3)
    nome=input('NOME: ')
    idade=int(input('IDADE: '))
    sexo=input('SEXO(H/M): ').strip().upper()
    soma +=idade
    if sexo=='H' and idade>velho:
        velho=idade
        nomevelho=nome
    if sexo=='M' and idade<20:
        contf+=1
print('A média de idade do grupo é {}'.format(soma/4))
print('O nome do homem mais velho é {} com {} anos'.format(nomevelho,velho))
print('Há nesse grupo {} mulheres com menos de 20 anos'.format(contf))