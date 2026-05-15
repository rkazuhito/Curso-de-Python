from time import sleep
def contador(n1,n2,p):
    p=abs(p)
    if n2>n1:
        c=n1
        while c<=n2:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c+=p
        print()
    else:
        c=n1
        while c>=n2:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c-=p
        print()
contador(1,10,1)
print('-'*15)
contador(10,0,2)
print('-'*15)
print('Agora temos um contador personalizado')
n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
p=int(input('Passo:'))
contador(n1,n2,p)