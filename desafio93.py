jogador={}
partidas=[]
jogador['nome']=input('Nome do Jogador: ')
jogador['golstotal']=0
tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1,tot+1):
    goles=int(input(f'Quantos gols na partida {c}?'))
    partidas.append(goles)
    jogador['golstotal']+=goles
jogador['gols']=partidas[:]
print('-='*15)
print(jogador)
print('-='*15)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'   -> Na partida {i} fez {v} gols')
print(f'Fez um total de {jogador['golstotal']} gols')