# ============================================================
# PROBLEMA 12 - Potencia por multiplicacoes sucessivas
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): base (int) e expoente (int maior ou igual a 0).
# Processamento: a funcao potencia(base, expoente) multiplica um
#   acumulador pela base, uma vez para cada unidade do expoente, sem usar
#   o operador **.
# Saida: o valor de base elevado a expoente.

# IMPLEMENTACAO
def potencia(base, expoente):
    resultado = 1
    contador = 1
    while contador <= expoente:
        resultado = resultado * base
        contador = contador + 1
    return resultado

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (inteiro maior ou igual a 0): "))

print(potencia(base, expoente))

# MICRODEFESA: por que iniciar resultado em 1 resolve tambem expoente zero?
# Porque 1 e o elemento neutro da multiplicacao e e tambem o valor
# matematico correto de qualquer base elevada a 0. Quando expoente e 0, o
# laco while nunca executa (contador comeca em 1 e ja e maior que 0),
# entao resultado permanece 1 sem precisar de nenhum caso especial extra.
