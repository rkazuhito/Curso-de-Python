print('\033[1;33;44m   FIBONACCI   \033[m')
termos=int(input('Gostaria de ver quantos termos da sequência de fibonacci? '))
n1=0
n2=1
print('{} -> {}'.format(n1,n2), end=' ')
x=3
while x<=termos:
    n3=n1+n2
    print(' -> {}'.format(n3), end=' ')
    n1=n2
    n2=n3
    x+=1