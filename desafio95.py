jogador={}
partidas=[]
time=[]
resp='S'
while resp=='S':
    jogador.clear()
    jogador['nome']=input('Nome do jogador: ')
    tot=int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}?')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    resp=input('Quer continuar? [S/N]').upper().strip()[0]
    while resp!='S' and resp!='N':
        print('Erro. Responda apenas S ou N')
        resp=input('Quer continuar? [S/N]').upper().strip()[0]

print('-='*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)

while True:
    busca=int(input('Mostrar os dados de qual jogador? [informe o código / 999 para] '))
    if busca==999:
        break
    if busca>=len(time):
        print(f'Erro. Não existe jogador com o código {busca}')
    else:
        print(f'   -- Levantamento do JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]):
            print(f'    No jogo {i+1} fez {g} gols')
        print('-'*40)
print('-'*40)
            