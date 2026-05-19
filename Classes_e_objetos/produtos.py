class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço inválido!")

    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
            print(f"Venda realizada! {quantidade} unidades vendidas.")
        else:
            print("Estoque insuficiente!")

    def __str__(self):
        return f"{self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque)"
    
    def mostrar(self):
        print(f"{self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque)")

produtos = []
for i in range(3):
    nome = input('Digite o nome do produto:')
    preco = int(input("DIgite o preço do produto:"))
    estoque = int(input('Digite a quantidade do produto:'))
    p = Produto(nome, preco, estoque)
    produtos.append(p)

for produto in produtos:
    produto.mostrar()