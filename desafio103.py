def ficha(nome='desconhecido',gols=0):
    print(f'O jogador {nome} fez {gols} gols')
nome=input('Nome do jogador: ')
gols=int(input('Número de gols: '))
ficha(nome, gols)