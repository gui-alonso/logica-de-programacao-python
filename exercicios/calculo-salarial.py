# Solicita ao usuário o salário atual
salario_atual = float(input("Digite o salário atual: "))

# Solicita ao usuário o percentual de reajuste
percentual_reajuste = float(input("Digite o percentual de reajuste (em %): "))

# Calcula o valor do reajuste
valor_reajuste = salario_atual * (percentual_reajuste / 100)

# Calcula o novo salário
novo_salario = salario_atual + valor_reajuste

# Exibe o valor do reajuste e o novo salário
print(f"O valor do reajuste é: R${valor_reajuste:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")