# calcular média de duas notas e determinar se o aluno está aprovado ou reprovado (media >= 7)

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
# nota3 = 3,6 (colocar ponto ao invés de vírgula)

resultado = (nota1 + nota2) / 2

print("a média foi: " + str(resultado))

# verifica se aluno foi aprovado ou reprovado

if (resultado >= 7):
    print("Aluno aprovado")
else:
    print("Aluno reprovado!")