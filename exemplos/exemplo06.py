"""
Escreva um programa que receba três notas de um aluno e calcule a média. Depois, determine se o aluno está aprovado, em recuperação ou reprovado, com base na média.

Aprovado >= 7
Em recuperação >= 5 OR < 7
Reprovado < 5
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

# verificar a média
if media >= 7:
    print(f"O aluno está aprovado! Média de {media:.2f}")
elif media <= 5:
    print(f"O aluno está em recuperação! Média de {media:.2f}")
else:
    print(f"O aluno está reprovado! Média de {media:.2f}")

# :.2f -> significa que queremos duas casas decimais,