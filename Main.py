from Cliente import Cliente
from Conta import Conta


class Main:
    pass


print('Testando o projeto')


c1 = Cliente('João', '144-222')
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, "Número: ", conta.numero, "Seu Saldo: ", conta.saldo)

# print(c1)
# print(c1.nome, " e ", c1.telefone)
