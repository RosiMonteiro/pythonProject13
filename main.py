from abc import ABC, abstractmethod

class FormaDePagamento(ABC):
    @abstractmethod
    def processarPagamento(self):
        pass

class CartaoCredito(FormaDePagamento):
    def processarPagamento(self):
        return "Pagamento com cartão de crédito processado."

class PayPal(FormaDePagamento):
    def processarPagamento(self):
        return "Pagamento com PayPal processado."

def escolher_forma_de_pagamento():
    print("Escolha a forma de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - PayPal")
    opcao = int(input("Digite o número da opção: "))

    if opcao == 1:
        return CartaoCredito()
    elif opcao == 2:
        return PayPal()
    else:
        print("Opção inválida.")
        return escolher_forma_de_pagamento()

def realizar_pagamento(forma_de_pagamento):
    print(forma_de_pagamento.processarPagamento())

if __name__ == '__main__':
    forma_de_pagamento = escolher_forma_de_pagamento()
    realizar_pagamento(forma_de_pagamento)
