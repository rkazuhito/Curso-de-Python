print('*-*'*10)
print('  Analisador de triângulos')
print('*-*'*10)
l1=float(input('\nDigite o primeiro lado: '))
l2=float(input('Agora o segundo: '))
l3=float(input('E o último: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Forma triângulo')
else:
    print('Não forma')