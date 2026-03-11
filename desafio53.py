print('='*10)
print('PALÍNDROMO')
print('='*10)
frase=input('Digite uma frase: ').upper().replace(' ','')
inverso=frase[::-1]
'''Abaixo como fazer com FOR'''
'''for letra in range(len(frase)-1,-1,-1):
    inverso += frase[letra]'''
print(frase, inverso)
if inverso == frase:
    print('Temos um palíndromo')
else:
    print('A frase não é palíndromo')