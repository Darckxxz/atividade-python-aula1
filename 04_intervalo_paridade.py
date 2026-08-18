# ============================================================
# PROBLEMA 4 - Intervalo e paridade
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um numero inteiro digitado pelo usuario.
# Processamento: calcula tres booleanos: se o numero esta entre 10 e 50
#   (inclusive), se e par, e se atende as duas condicoes ao mesmo tempo
#   (usando "and").
# Saida: os tres booleanos, um por linha, com o rotulo indicado.

# IMPLEMENTACAO
numero = int(input("Digite um número inteiro: "))

no_intervalo = numero >= 10 and numero <= 50
par = numero % 2 == 0
duas_regras = no_intervalo and par

print(f"Está no intervalo: {no_intervalo}")
print(f"É par: {par}")
print(f"Atende às duas regras: {duas_regras}")

# MICRODEFESA: qual seria o erro logico se a terceira regra usasse or?
# Com "or", a terceira regra seria verdadeira sempre que qualquer uma das
# duas condicoes fosse verdadeira sozinha, mesmo sem a outra. Isso faria,
# por exemplo, o numero 11 (par? nao, mas esta no intervalo) ser
# classificado como atendendo "as duas regras" mesmo sem ser par, o que
# contraria o significado de "atender as duas regras ao mesmo tempo".
