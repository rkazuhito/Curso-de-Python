escolha=1
print('\033[1;33;44m   CALCULADORA   \033[m')
n1=float(input('Primeiro valor: '))
n2=float(input('Segundo valor: '))
while escolha!=6:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] MENOR')
    print('[5] NOVOS VALORES')
    print('[6] SAIR')
    escolha=int(input('>>>  Qual a sua escolha? '))
    if escolha==1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif escolha==2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif escolha==3:
        if n1>n2:
            print('{} > {}'.format(n1,n2))
        elif n2>n1:
            print('{} > {}'.format(n2,n1))
        else:
            print('{} = {}'.format(n1,n2))
    elif escolha==4:
        if n1<n2:
           print('{} < {}'.format(n1,n2))
        elif n2>n1:
            print('{} < {}'.format(n2,n1))
        else:
            print('{} = {}'.format(n1,n2))
    elif escolha==5:
        n1=float(input('Primeiro valor: '))
        n2=float(input('Segundo valor: '))