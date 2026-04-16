ver='S'
pessoas=[]
dados=['nome',0]
pesadas=[]
leves=[]
totpes=0
while ver=='S':
    dados[0]=input('Nome: ')
    dados[1]=float(input('Peso: '))
    if dados[1]>=100:
        pesadas.append(dados[0])
    elif dados[1]<=70:
        leves.append(dados[0])
    pessoas.append(dados[:])
    dados.clear
    totpes+=1
    ver=input('Deseja continuar? [s/n]').upper().strip()[0]
print(f'Você registrou as pessoas {pessoas} \nAo todo foram {totpes}')
print(f'As mais pesadas foram as {pesadas}')
print(f'E as mais leves foram as {leves}')