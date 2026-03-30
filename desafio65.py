n=int(input('Digite um número'))
tot=1
soma=n
maior=n
menor=n
resposta=input('Deseja continuar? [S/N]').upper().strip()[:1]
while resposta=='S':
    n=int(input('Digite um número'))
    tot+=1
    soma=soma+n
    if n>maior:
        maior=n
    if n<menor:
        menor=n
    resposta=input('Deseja continuar? [S/N]').upper().strip()[:1]
print('Você digitou {} números, a média entre eles foi {:.1f}'.format(tot,soma/tot))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))