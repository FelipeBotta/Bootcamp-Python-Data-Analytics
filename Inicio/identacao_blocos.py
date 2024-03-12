def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado !")
        saldo -= valor
        print(f"Seu saldo eh {saldo}")
    
    print("Obrigado por utilizar nosso Banco !")


def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Realizamos o deposito de {valor} e agora seu saldo eh de {saldo}")

depositar(1000)