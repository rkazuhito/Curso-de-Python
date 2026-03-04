cat1=float(input('Qual a medida do cateto? '))
cat2=float(input('Qual a medida do outro cateto? '))
hip=(cat1**2+cat2**2)**(1/2)
print('A hipotenusa vale {:.2f}'.format(hip))