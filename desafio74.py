import random
tupla=(random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
maior=0
menor=101
for c in range(0,len(tupla)):
    print(tupla[c], end=' ')
    if tupla[c]>maior:
        maior=tupla[c]
    if tupla[c]<menor:
        menor=tupla[c]
print(f'\nO maior valor dessa tupla foi o {maior} e o menor foi o {menor}')