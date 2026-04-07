palavras=('teste', 'programar', 'aprender', 'python', 'macaco','cebola','passado','marceneiro','academia','pokemon','sol', 'praticar')
for c in range(0,len(palavras)):
    print(f'\nNa palavras {palavras[c].upper()} temos', end=' ')
    for letra in palavras[c]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')