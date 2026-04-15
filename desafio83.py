print('Verificador de expressões')
expressao=input('Digite sua expressão: ')
contabre=contfecha=0
for c in range(0,len(expressao)):
    if expressao[c]=='(':
        contabre+=1
    elif expressao[c]==')':
        contfecha+=1
if contabre==contfecha:
    print('Expressão válida')
else:
    print('Expressão inválida')