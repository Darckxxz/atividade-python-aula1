# ============================================================
# PROBLEMA 7 - Fatorial e os casos 0! e 1!
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro n maior ou igual a 0.
# Processamento: multiplica sucessivamente um acumulador pelos numeros de
#   1 ate n usando while; se n for 0, o laco nao executa nenhuma vez.
# Saida: o valor de n!.

# IMPLEMENTACAO
n = int(input("Digite um número inteiro maior ou igual a 0: "))

fatorial = 1
contador = 1
while contador <= n:
    fatorial = fatorial * contador
    contador = contador + 1

print(fatorial)

# MICRODEFESA: por que o acumulador do produto deve comecar em 1?
# Porque 1 e o elemento neutro da multiplicacao: multiplicar por 1 nao
# altera o valor. Se o acumulador comecasse em 0, qualquer numero
# multiplicado por 0 permaneceria 0 para sempre, destruindo o calculo.
# Comecar em 1 tambem garante que 0! resulte corretamente em 1, ja que
# nesse caso o laco nunca executa e o acumulador permanece inalterado.
