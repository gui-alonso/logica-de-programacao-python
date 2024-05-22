# reajuste salarial

# Solicitar o salário atual do funcionário
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

# Solicitar a taxa de reajuste em porcentagem
taxa_reajuste = float(input("Digite a taxa de reajuste (%): "))

# Calcular o valor do reajuste
valor_reajuste = salario_atual * (taxa_reajuste / 100)

# Calcular o novo salário
novo_salario = salario_atual + valor_reajuste

# Exibir o resultado
print(f"O valor do reajuste é de R$ {valor_reajuste:.2f}")
print(f"O novo salário do funcionário é de R$ {novo_salario:.2f}")