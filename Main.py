from Cliente import Cliente
from Conta import Conta


class Main:
    pass


print('Testando o projeto')


c1 = Cliente('João', '144-222')
conta = Conta(c1._nome, 6565, 0)

print(conta._titular, "Número: ", conta._numero, "Seu Saldo: ", conta._saldo)

# print(c1)
# print(c1.nome, " e ", c1.telefone)
