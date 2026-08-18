# ============================================================
# PROBLEMA 15 - Palindromo preservando o valor original
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro positivo.
# Processamento: a funcao eh_palindromo(numero) guarda o valor original
#   em outra variavel, usa uma copia separada para extrair digitos (% 10
#   e // 10) e reconstroi o valor invertido, sem alterar o original.
# Saida: True se o invertido for igual ao original, False caso contrario;
#   o programa exibe "Palíndromo" ou "Não palíndromo".

# IMPLEMENTACAO
def eh_palindromo(numero):
    original = numero
    resto = numero
    invertido = 0
    while resto > 0:
        digito = resto % 10
        invertido = invertido * 10 + digito
        resto = resto // 10
    return invertido == original

numero = int(input("Digite um número inteiro positivo: "))

if eh_palindromo(numero):
    print("Palíndromo")
else:
    print("Não palíndromo")

# MICRODEFESA: qual valor precisa ser preservado e por que?
# O valor original de "numero" precisa ser preservado em uma variavel
# separada ("original") porque o processo de inversao consome a copia de
# trabalho ("resto") ate ela chegar a 0. Se a comparacao final usasse a
# mesma variavel que foi alterada durante o laco, ela estaria comparando
# o invertido contra 0 (ou contra um valor ja modificado), e nao contra o
# numero realmente digitado, tornando a comparacao incorreta.
