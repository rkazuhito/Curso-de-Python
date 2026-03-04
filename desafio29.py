v=float(input('Qual a velocidade do carro? (Km/h)'))
if v>80:
    multa=(v-80)*7
    print('Você foi multado em R${:.2f} por andar {:.2f}Km/h acima do limite'.format(multa,v-80))
else:
    print('Você não foi multado')
print('Drive safe')