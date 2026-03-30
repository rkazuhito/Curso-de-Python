print('\033[1;33;44m   FLAG   \033[m')
n=int(input('Digite um valor [999 para sair]: '))
soma=n
tot=1
while n!=999:
    n=int(input('Digite um valor [999 para sair]: '))
    if n==999:
        break
    soma+=n
    tot+=1
print(f'A soma dos {tot} valores foi {soma}')