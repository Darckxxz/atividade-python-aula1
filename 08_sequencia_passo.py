# ============================================================
# PROBLEMA 8 - Sequencia definida por passo
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): inicio, passo e quantidade (int, quantidade >= 1).
# Processamento: gera "quantidade" valores comecando em "inicio" e
#   somando "passo" a cada repeticao, controlando o numero de iteracoes
#   com um contador (sem armazenar a sequencia em uma colecao).
# Saida: os valores gerados, separados por virgula, em uma unica linha.

# IMPLEMENTACAO
inicio = int(input("Digite o valor inicial: "))
passo = int(input("Digite o passo: "))
quantidade = int(input("Digite a quantidade de valores (maior ou igual a 1): "))

valor = inicio
contador = 1
saida = ""
while contador <= quantidade:
    if contador == 1:
        saida = f"{valor}"
    else:
        saida = saida + ", " + f"{valor}"
    valor = valor + passo
    contador = contador + 1

print(saida)

# MICRODEFESA: por que quantidade controla o numero de repeticoes, e nao
# o valor final da sequencia?
# Porque "quantidade" e usada apenas para comparar com o contador de
# iteracoes do while (quanto laços ainda faltam rodar), nunca com o
# proprio valor gerado. O valor final da sequencia depende de inicio e
# passo (inicio + passo multiplicado pelo numero de repeticoes), entao
# tratar quantidade como se fosse um limite numerico de valor misturaria
# duas ideias diferentes: "quantas vezes repetir" e "ate onde os valores
# chegam".
