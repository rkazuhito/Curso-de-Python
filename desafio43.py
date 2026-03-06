print('- -'*10)
print('\033[1;46m      Calculadora de IMC      \033[m')
print('- -'*10)
p=float(input('Qual seu peso? '))
h=float(input('Qual sua altura? '))
imc=p/(h**2)
if imc<18.5:
    print('Seu IMC é {:.1f} e está \033[33mabaixo do peso\033[m'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é {:.1f} e você está com \033[32mpeso normal\033[m'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é {:.1f} e você está com \033[33msobrepeso\033[m'.format(imc))
elif imc>=30 and imc<40:
    print('Seu IMC é {:.1f} e você está com \033[31mobesidade\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com \033[41mobesidade grave\033[m'.format(imc))