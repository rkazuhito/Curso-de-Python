print('\033[1;33;44m   CADASTRO RH   \033[m')
maior=homem=mulhermenor=tot=0
while True:
    print('--'*15)
    print('Cadastre uma pessoa:')
    print('--'*15)
    idade=int(input('IDADE: '))
    if idade>=18:
        maior+=1
    sexo=input('SEXO [M/F]: ').strip().upper()[:1]
    if sexo=='M':
        homem+=1
    if sexo=='F' and idade<20:
        mulhermenor+=1
    tot+=1
    escolha=input('Deseja cadastrar mais uma pessoa? [S/N] ').strip().upper()[:1]
    if escolha=='N':
        break
print(f'Ao todo foram cadastrados {tot} pessoas, sendo {maior} maiores de 18 anos, {homem} homens e {mulhermenor} mulheres com menos de 20 anos')