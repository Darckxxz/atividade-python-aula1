# ============================================================
# PROBLEMA 9 - Numero primo sem interrupcao antecipada
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): um inteiro n maior que 1.
# Processamento: percorre todos os inteiros de 1 ate n (sem break),
#   contando quantos deles dividem n exatamente (resto 0).
# Saida: "Primo" se o total de divisores for exatamente 2, senao
#   "Não primo".

# IMPLEMENTACAO
n = int(input("Digite um número inteiro maior que 1: "))

contador_divisores = 0
divisor = 1
while divisor <= n:
    if n % divisor == 0:
        contador_divisores = contador_divisores + 1
    divisor = divisor + 1

if contador_divisores == 2:
    print("Primo")
else:
    print("Não primo")

# MICRODEFESA: quais sao os dois divisores de um numero primo?
# Sao o numero 1 e o proprio numero. Como a regra de decisao e "exatamente
# dois divisores", tanto o 1 quanto o proprio n precisam ser incluidos na
# contagem (o laco vai de 1 ate n, sem parar antes), pois excluir qualquer
# um deles faria a contagem nunca chegar a 2 mesmo para numeros primos.
