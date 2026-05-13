def escreva(frase):
    tamanho=len(frase)+4
    print('-'*tamanho)
    print(f'{frase:^{tamanho}}')
    print('-'*tamanho)
escreva('Teste')
escreva('Olá, mundo!')
escreva('Teste de frase um pouco mais para centralizar')