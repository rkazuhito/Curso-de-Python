contagem=('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'quatorze',  'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
n=int(input('Digite um número entre 0 e 20: '))
while True:
    if n>20 or n<0:
        n=int(input('Valor incorreto. Digite um número entre 0 e 20: '))
    else:
        print(contagem[n])
        break
