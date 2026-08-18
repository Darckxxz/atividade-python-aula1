# ============================================================
# PROBLEMA 10 - Funcao de classificacao numerica
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um numero inteiro lido do usuario.
# Processamento: a funcao classificar_numero(numero) decide primeiro se o
#   valor e zero; caso nao seja, decide o sinal e depois a paridade,
#   retornando a string correspondente.
# Saida: uma das cinco strings de classificacao, exibida apos o retorno
#   da funcao ser armazenado em uma variavel.

# IMPLEMENTACAO
def classificar_numero(numero):
    if numero == 0:
        resultado = "zero"
    elif numero > 0 and numero % 2 == 0:
        resultado = "positivo e par"
    elif numero > 0:
        resultado = "positivo e ímpar"
    elif numero % 2 == 0:
        resultado = "negativo e par"
    else:
        resultado = "negativo e ímpar"
    return resultado

numero = int(input("Digite um número inteiro: "))
classificacao = classificar_numero(numero)
print(classificacao)

# MICRODEFESA: por que zero nao deve cair nas categorias positivo/negativo?
# Porque zero nao e maior nem menor que zero, entao testes como
# "numero > 0" ou "numero < 0" sao ambos falsos para ele. Sem uma decisao
# propria (testar "numero == 0" primeiro), o zero acabaria caindo por
# eliminacao em uma categoria de sinal que nao lhe pertence, ou exigiria
# logica extra e confusa para ser tratado corretamente.
