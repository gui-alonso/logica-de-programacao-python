# conversor de moeda

# Taxa de câmbio
taxa_usd_brl = 5.1538  # 1 dólar = 5.15 reais

# Entrada do usuário
opcao = input("Escolha a conversão:\n a) Real para USD\n b) USD para Real\n").lower()

if opcao == 'a':
    real = float(input("Quanto dinheiro você tem na carteira? R$ "))
    dolar = real / taxa_usd_brl
    print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real, dolar))
elif opcao == 'b':
    dolar = float(input("Quantos dólares você tem? $ "))
    real = dolar * taxa_usd_brl
    print("Com US$ {:.2f} você pode comprar R$ {:.2f}".format(dolar, real))
else:
    print("Opção inválida!")