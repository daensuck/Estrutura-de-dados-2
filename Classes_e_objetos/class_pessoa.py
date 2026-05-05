class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida!")

    def apresentar(self):
        print(f"Olá! Meu nome é {self.__nome} e tenho {self.__idade} anos.")

pessoas = []
for i in range(3):
   nome = input("Digite o nome da pessoa: ")
   idade = int(input("Digite a idade da pessoa: "))
   p = Pessoa(nome, idade)
   pessoas.append(p)
for pessoa in pessoas:
   pessoa.apresentar()