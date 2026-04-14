lista=[]
verificador='S'
cont=0
while verificador=='S':
    lista.append(input('Digite um valor: '))
    cont+=1
    verificador=input('Deseja continuar? [S/N]').upper().strip()[0]
print(f'Ao todo foram digitados {cont} numeros na lista')
lista.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente ficou: {lista}')
if 5 in lista:
    print('Foi digitado o número 5')
else:
    print('Não houve nenhuma ocorrência do número 5')