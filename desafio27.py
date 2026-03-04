nome=input('Digite seu nome completo: ').strip()
nomeseparado=nome.split()
print('O seu primeiro nome é {}'.format(nomeseparado[0]))
print('O último nome é {}'.format(nomeseparado[nome.count(' ')]))