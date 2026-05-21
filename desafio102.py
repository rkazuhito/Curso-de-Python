from time import sleep
def fatorial(fat,ver=1):
    c=fat
    calculo=1
    if ver==1:
        while c>1:
            calculo=c*calculo
            print(f'{c} x' ,end=' ', flush=True)
            sleep(0.5)
            c-=1
        print('1 =', end=' ', flush=True)
        sleep(0.5)
        return calculo
    if ver==0:
        while c>1:
            calculo=c*calculo
            c-=1
        return calculo
print('Cálculo de fatorial')
print('-'*15)
num=int(input('Qual valor deseja calcular? '))
verificador=int(input('Deseja ver o processo do cálculo? (1 para SIM ou 0 para NÃO)'))
result=fatorial(num,verificador)
print(result)