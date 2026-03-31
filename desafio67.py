print('\033[1;33;44m   TABUADA 3.0   \033[m')
n=int(input('Quer ver a tabuada de qual valor? '))
print('--'*20)
while n>=0:
    for x in range(1,11):
        print(f'{n} X {x} = {n*x}')
    print('--'*20)
    n=int(input('Quer ver a tabuada de qual valor? '))
    print('--'*20)