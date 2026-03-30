print('\033[1;33;44m   TRATANDO VÁRIOS VALORES   \033[m')
n=int(input('Digite um número [999 para sair]: '))
if n!=999:
    soma=n
    cont=1
else:
    soma=0
    cont=0
while n!=999:
    n=int(input('Digite um número [999 para sair]: '))
    if n!=999:
        soma=soma+n
        cont+=1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))