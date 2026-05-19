class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade
    
    def acelerar(self):
        print('O carro está acelerando:')

    def frear(self):
        print('O carro está freando.')

    def mostrar(self):
        print(f"Marca: {self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque)")