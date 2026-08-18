# ============================================================
# PROBLEMA 3 - Maior e menor com empates parciais
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): tres numeros inteiros a, b e c.
# Processamento: se os tres forem iguais, sinaliza esse caso; caso
#   contrario, encontra o maior e o menor comparando cada valor com um
#   acumulador, sem usar min()/max().
# Saida: "Todos iguais" ou o maior valor seguido do menor valor.

# IMPLEMENTACAO
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b and b == c:
    print("Todos iguais")
else:
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c

    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c

    print(maior)
    print(menor)

# MICRODEFESA: por que testar apenas a > b and a > c nao e suficiente?
# Porque quando ha empate no valor maximo (por exemplo, 4, 9, 9), nenhum
# dos elementos empatados e estritamente maior que os outros dois ao
# mesmo tempo, entao essa condicao isolada nunca seria verdadeira para o
# valor que na verdade e o maior. A comparacao incremental (atualizar o
# acumulador sempre que um valor maior aparece) resolve isso porque nao
# depende de um unico elemento vencer todos os outros de uma so vez.
