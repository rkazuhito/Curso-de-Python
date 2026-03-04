l=float(input('Qual a largura da parede em metros? '))
h=float(input('Qual a altura da parede em metros?'))
a=h*l
print('A sua parede tem uma área de {:.2f}m²'.format(a))
tinta=a/2
print('Para pintar essa parede você vai precisar de {}l de tinta'.format(tinta))