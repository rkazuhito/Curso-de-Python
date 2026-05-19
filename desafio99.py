def maior(*numeros):
    for c in range(0,len(numeros)):
        if c==0:
            maior=numeros[c]
        else:    
            if numeros[c]>maior:
                maior=numeros[c]
    print(f'Ao todo foram digitados {len(numeros)} números')
    print(f'O maior valor foi o {maior}')
maior(1,5,3,9,7,6,4,2,50,10,7,3)
print('-'*20)
maior(-2,-5,-9,-7,-6,-15)
