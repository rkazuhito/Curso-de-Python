sal=float(input('Qual o salário? '))
if sal>1250:
    salnovo=sal*1.1
else:
    salnovo=sal*1.15
print('O salário novo ficou em R${:.2f}'.format(salnovo))