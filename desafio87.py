matriz=[[0,0,0],[0,0,0],[0,0,0]]
par=somaterceirac=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor para a posição [{l}][{c}]'))
        if matriz[l][c]%2==0:
            par+=matriz[l][c]
        if c==2:
            somaterceirac+=matriz[l][c]
        if l==1:
            if c==0:
               maiorsegundal=matriz[l][c] 
            elif matriz[l][c]>maiorsegundal:
                maiorsegundal=matriz[l][c]
print('--'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('--'*20)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {somaterceirac}')
print(f'O maior valor da seunda linha é o {maiorsegundal}')