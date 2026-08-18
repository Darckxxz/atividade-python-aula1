# ============================================================
# PROBLEMA 1 - Classificacao da media nas fronteiras
# ============================================================

# PREVISAO E DECOMPOSICAO
# Entrada(s): tres notas (float) digitadas pelo usuario.
# Processamento: soma as tres notas e divide por 3 para obter a media;
#   compara a media com as fronteiras 4, 6 e 9, da menor para a maior,
#   usando if/elif/else.
# Saida: a media formatada com duas casas decimais e a classificacao
#   correspondente.

# IMPLEMENTACAO
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
    classificacao = "Reprovado"
elif media < 6:
    classificacao = "Recuperação"
elif media < 9:
    classificacao = "Aprovado"
else:
    classificacao = "Aprovado com destaque"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")

# MICRODEFESA: por que a ordem das condicoes pode alterar a classificacao?
# Porque a cadeia usa elif: cada condicao so e avaliada se a anterior for
# falsa. Se a ordem fosse trocada (por exemplo, testar "media < 9" antes de
# "media < 6"), uma media igual a 5 cairia nessa primeira condicao
# verdadeira e receberia "Aprovado" em vez de "Recuperação", pois o elif
# nunca chega a avaliar a condicao correta depois de encontrar uma
# verdadeira antes dela.
