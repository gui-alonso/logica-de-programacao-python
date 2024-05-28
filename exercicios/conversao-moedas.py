def brl_to_usd(amount):
    # Cotação atual BRL para USD (apenas uma estimativa)
    exchange_rate = 0.1938
    converted_amount = amount * exchange_rate
    return converted_amount

def usd_to_brl(amount):
    # Cotação atual USD para BRL (apenas uma estimativa)
    exchange_rate = 5.1602  # Um valor fictício para demonstração
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. BRL para USD")
        print("2. USD para BRL")
        print("3. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            brl_amount = float(input("Digite o valor em BRL: "))
            usd_amount = brl_to_usd(brl_amount)
            print(f"O valor convertido é aproximadamente {usd_amount:.2f} USD")
        elif choice == '2':
            usd_amount = float(input("Digite o valor em USD: "))
            brl_amount = usd_to_brl(usd_amount)
            print(f"O valor convertido é aproximadamente {brl_amount:.2f} BRL")
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()