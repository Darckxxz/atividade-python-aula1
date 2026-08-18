# ============================================================
# PROBLEMA 5 - Contagem regressiva seletiva
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro n maior ou igual a 0.
# Processamento: usando somente while, percorre os valores de n ate 0,
#   decrescendo uma unidade a cada iteracao; quando o valor atual e maior
#   que 0 e divisivel por 5, prepara uma mensagem especial.
# Saida: cada numero de n ate 0, um por linha, com aviso quando divisivel
#   por 5.

# IMPLEMENTACAO
n = int(input("Digite um número inteiro maior ou igual a 0: "))

atual = n
while atual >= 0:
    if atual > 0 and atual % 5 == 0:
        print(f"{atual} é divisível por 5")
    else:
        print(atual)
    atual = atual - 1

# MICRODEFESA: qual linha garante que o while possa terminar?
# A linha "atual = atual - 1" garante o termino, pois aproxima "atual" da
# condicao de parada "atual >= 0" a cada iteracao; sem essa atualizacao,
# "atual" nunca mudaria e o laco rodaria para sempre.
