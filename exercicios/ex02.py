# Calcular a média de duas notas e determinar se o aluno está aprovado ou reprovado (média >= 7)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")