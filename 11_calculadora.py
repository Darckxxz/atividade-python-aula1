# ============================================================
# PROBLEMA 11 - Calculadora e retorno None
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): dois numeros a e b, e uma operacao (str) entre + - * /.
# Processamento: a funcao calcular(a, b, operacao) executa a operacao
#   reconhecida; retorna None quando a operacao nao e reconhecida ou
#   quando ha tentativa de divisao por zero.
# Saida: o resultado da operacao, ou "Operação inválida" quando o retorno
#   for None.

# IMPLEMENTACAO
def calcular(a, b, operacao):
    resultado = None
    if operacao == "+":
        resultado = a + b
    elif operacao == "-":
        resultado = a - b
    elif operacao == "*":
        resultado = a * b
    elif operacao == "/":
        if b != 0:
            resultado = a / b
        else:
            resultado = None
    else:
        resultado = None
    return resultado

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = calcular(a, b, operacao)

if resultado is None:
    print("Operação inválida")
else:
    print(resultado)

# MICRODEFESA: por que print dentro da funcao nao substitui return?
# Porque print apenas exibe um valor na tela naquele momento e a funcao
# termina sem entregar nada a quem a chamou; a variavel que recebeu a
# chamada (resultado = calcular(...)) ficaria com None. O return e o que
# devolve o valor calculado para fora da funcao, permitindo que o
# programa guarde, compare (por exemplo, "is None") ou reutilize esse
# valor depois.
