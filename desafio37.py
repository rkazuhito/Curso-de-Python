print('=-'*15)
print('\033[1;31;43m Conversor de bases numéricas \033[m')
print('=-'*15)
n=int(input('Informe um valor: '))
escolha=int(input('Você quer transformar esse número para qual base? \n[1]Binário \n[2]Octal \n[3]Hexadecimal \nSua opção: '))
if escolha==1:
    print(bin(n)[2:])
elif escolha==2:
    print(oct(n)[2:])
elif escolha==3:
    print(hex(n)[2:])
else:
    print('Escolha um número do menu!!')