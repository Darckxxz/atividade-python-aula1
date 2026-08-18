# ============================================================
# PROBLEMA 13 - Soma dos digitos sem str
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro positivo.
# Processamento: usando somente % e //, extrai o ultimo digito do numero
#   a cada repeticao (resto da divisao por 10), soma-o a um acumulador, e
#   remove esse digito do numero (divisao inteira por 10), sem converter
#   nada para str.
# Saida: a soma de todos os digitos do numero.

# IMPLEMENTACAO
n = int(input("Digite um número inteiro positivo: "))

soma = 0
resto = n
while resto > 0:
    digito = resto % 10
    soma = soma + digito
    resto = resto // 10

print(soma)

# MICRODEFESA: o que % 10 extrai e o que // 10 remove?
# "% 10" extrai o resto da divisao por 10, que corresponde exatamente ao
# ultimo digito (o digito das unidades) do numero. "// 10" faz a divisao
# inteira por 10, descartando esse ultimo digito e deslocando os demais
# digitos uma casa para a direita, preparando o numero para a proxima
# extracao.
