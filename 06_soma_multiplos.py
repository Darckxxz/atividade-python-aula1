# ============================================================
# PROBLEMA 6 - Soma de multiplos sem divisor zero
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): limite (int >= 1) e divisor (int diferente de 0).
# Processamento: percorre com for/range todos os inteiros de 1 ate
#   limite, inclusive, somando ao acumulador aqueles que sao divisiveis
#   pelo divisor.
# Saida: a soma final dos multiplos encontrados.

# IMPLEMENTACAO
limite = int(input("Digite o limite (maior ou igual a 1): "))
divisor = int(input("Digite o divisor (diferente de 0): "))

soma = 0
for numero in range(1, limite + 1):
    if numero % divisor == 0:
        soma = soma + numero

print(soma)

# MICRODEFESA: por que o acumulador precisa ser inicializado?
# Porque "soma = soma + numero" depende de um valor anterior de soma para
# calcular o proximo; se soma nao existisse antes do for, essa expressao
# nao teria com o que somar. Alem disso, o valor inicial precisa ser 0
# porque 0 e o elemento neutro da adicao, garantindo que o primeiro
# multiplo encontrado seja somado sem alterar o resultado esperado.
