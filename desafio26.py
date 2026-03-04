frase=input('Digite a sua frase: ').lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que A aparece é na posição {} (contagem começa e 0)'.format(frase.find('a')))
print('A última vez é na posição {}'.format(frase.rfind('a')))