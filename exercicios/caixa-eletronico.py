class Conta:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de R${valor} para {destino.nome} realizada. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente para transferência.")

    def verificar_saldo(self):
        print(f"Saldo atual da conta de {self.nome}: R${self.saldo}")


def main():
    # Criando algumas contas para teste
    conta1 = Conta("João", 1000)
    conta2 = Conta("Maria", 500)

    while True:
        print("\n--- Menu ---")
        print("1. Verificar saldo")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Transferir dinheiro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            conta1.verificar_saldo()
        elif escolha == '2':
            valor = float(input("Digite o valor a ser depositado: "))
            conta1.depositar(valor)
        elif escolha == '3':
            valor = float(input("Digite o valor a ser sacado: "))
            conta1.sacar(valor)
        elif escolha == '4':
            destino = input("Digite o nome do destinatário: ")
            valor = float(input("Digite o valor a ser transferido: "))
            if destino.lower() == conta2.nome.lower():
                conta1.transferir(conta2, valor)
            else:
                print("Conta de destino não encontrada.")
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()