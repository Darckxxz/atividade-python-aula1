# ============================================================
# PROBLEMA 2 - Ano bissexto: o caso 1900
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um ano (int) digitado pelo usuario.
# Processamento: testa a divisibilidade por 400, depois por 100 e por 4,
#   nessa ordem, aplicando exatamente as regras do enunciado.
# Saida: "Bissexto" ou "Não bissexto".

# IMPLEMENTACAO
ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    resultado = "Bissexto"
elif ano % 100 == 0:
    resultado = "Não bissexto"
elif ano % 4 == 0:
    resultado = "Bissexto"
else:
    resultado = "Não bissexto"

print(resultado)

# MICRODEFESA: por que testar somente divisibilidade por 4 e insuficiente?
# Porque anos como 1900 e 2100 sao divisiveis por 4, mas tambem sao
# divisiveis por 100 e nao por 400, entao a regra correta os classifica
# como "Não bissexto". Testar apenas "ano % 4 == 0" ignoraria essa
# excecao e classificaria 1900 e 2100 erradamente como bissextos.
