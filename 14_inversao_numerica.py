# ============================================================
# PROBLEMA 14 - Inversao numerica e zeros a direita
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro positivo.
# Processamento: extrai os digitos do numero da direita para a esquerda
#   (usando % 10 e // 10) e os reconstroi em um acumulador multiplicado
#   por 10 a cada passo, sem converter nada para str.
# Saida: o inteiro com os digitos invertidos (sem zeros a esquerda, pois
#   e um inteiro).

# IMPLEMENTACAO
n = int(input("Digite um número inteiro positivo: "))

resto = n
invertido = 0
while resto > 0:
    digito = resto % 10
    invertido = invertido * 10 + digito
    resto = resto // 10

print(invertido)

# MICRODEFESA: por que 1200 invertido numericamente resulta em 21?
# Porque os primeiros digitos extraidos de 1200 (da direita para a
# esquerda) sao 0 e 0. Multiplicar o acumulador "invertido" (que comeca
# em 0) por 10 e somar 0 mantem o acumulador em 0, entao esses zeros nao
# deixam nenhum registro na construcao do numero. Somente quando aparecem
# os digitos 2 e 1 o acumulador passa a crescer, resultando em 21 em vez
# de 0021, porque um inteiro nunca guarda zeros a esquerda.
