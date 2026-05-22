def notas(*n, sit=False):
    soma=0
    for c in range(0,len(n)):
        if c==0:
            maior=n[c]
            menor=n[c]
        if n[c]>maior:
            maior=n[c]
        if n[c]<menor:
            menor=n[c]
        soma+=n[c]
    media=soma/len(n)
    dict={}
    dict['Quantidade de notas']=len(n)
    dict['A maior nota']=maior
    dict['A menor nota']=menor
    dict['A média da turma']=media
    if sit==True:
        if media<5:
            dict['Situação']='RUIM'
        elif media<7:
            dict['Situação']='MÉDIA'
        else:
            dict['Situação']='ÓTIMO'
    return dict
#main
print(notas(10,5,9,3,sit=True))