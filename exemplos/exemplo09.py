"""
Faça um programa de conversor de moeda. O usuário deve escolher dentre as opções:

1. BRL para US$
2. US$ para BRL
3. sair

Enquanto o usuário não digitar 3 o programa deve continuar normalmente, caso o usuário digite 3, o programa deve-se encerrar.
"""

taxa_brl_para_usd = 5.29 # 1 USD = 5.29 BRL
taxa_usd_para_brl = 1 / taxa_brl_para_usd # 1 BRL = 0.20 USD

while True:
    #Exibe o menu de opções
   print("\n Escolha uma opção: ")
   print("1. BRL para US$")
   print("2. US$ para BRL")
   print("3. Sair")

   opcao = input("Digite o número da opção desejada: ")

   if opcao == '1':
      valor_brl = float(input("Digite o valor em (R$): "))
      valor_usd = valor_brl / taxa_brl_para_usd
      print(f"R$ {valor_brl:.2f}  é equivalente a US$ {valor_usd:.2f}")
   elif opcao == '2':
      valor_usd = float(input("Digite o valor em dólares (US$): "))
      valor_brl = valor_usd * taxa_brl_para_usd
      print(f"US$ {valor_usd:.2f} é equivalente a R$ {valor_brl:.2f}")
   elif opcao == '3':
      print("Saindo...")
      break
   else:
      print("Opção inválida.. Tente novamente.")   


# --------------------------------------------

"""
### Explicação do Código:

1. Taxas de Câmbio Fixas: As taxas de câmbio são definidas no início do código.
2. Loop Principal:
   - Um loop `while` que continua até que o usuário escolha sair (`opcao == '3'`).
   - Dentro do loop, o menu é exibido e o usuário insere sua escolha.
   - Se o usuário escolhe `1`, o programa pede um valor em reais, converte para dólares e exibe o resultado.
   - Se o usuário escolhe `2`, o programa pede um valor em dólares, converte para reais e exibe o resultado.
   - Se o usuário escolhe `3`, o programa imprime uma mensagem de saída e interrompe o loop.
   - Se o usuário insere uma opção inválida, o programa exibe uma mensagem de erro.
"""