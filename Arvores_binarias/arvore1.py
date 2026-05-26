class NO:
    def __init__(self,info):
        self.info = info
        self.esq = None
        self.dir = None
        print("<",self.esq," ",self.info, " ", self.dir,">" )
    
    def insere_dir(self,num):
        self.dir = NO(num)


class ArvBin:
    def __init__(self):
        self.__raiz = None

    def insere(self,valor):
        novo = NO(valor)
        if self.__raiz == None:
            self.__raiz = novo
        else: 
            atual = self.__raiz
            anterior = None
        
            while atual != None:


                anterior = atual
                if valor > atual.info:
                    atual = atual.dir
                else:
                    atual = atual.esq
            if valor > anterior.info:
                anterior.dir = novo
            else:
                anterior.esq = novo
        return True

    def pre_ordem(self):
        if  self.__raiz != None:
            self._pre_ordem(self.__raiz)
    
    def _pre_ordem(self,raiz):
        if not raiz:
            return
        # Visita nodo corrente.
        print(raiz.info)
        # Visita filho da esquerda.
        self._pre_ordem(raiz.esq)
        # Visita filho da direita.
        self._pre_ordem(raiz.dir)

    def menorValor(self):
        if self.__raiz == None:
            return False
        
        else: 
            menor = self.__raiz
            while menor.esq != None:
                menor = menor.esq
            return print(menor.info)
        
    def bucaValor(self,valor):
        if self.__raiz == None:
            return False
        
        atual = self.__raiz
        while atual != None:
            if atual.info == valor:
                return True
            if atual.info > valor:
                atual = atual.dir
            else:
                atual = atual.esq

        return False
    
    def imprimeCaminhos(self):
        # lista para armazenar os caminhos raiz-folha
        lista = []
        self.__imprimeCaminhosRec(self.__raiz,lista)

    def __imprimeCaminhosRec(self, raiz, lista):
        if raiz is None:   #arvore vazia, retornar!
            return
        lista.append(raiz.info)    #inserir ao final da lista
        if raiz.esq is None and raiz.dir is None:
            print(lista)
        else:
            if raiz.esq: self.__imprimeCaminhosRec(raiz.esq, lista)
            if raiz.dir: self.__imprimeCaminhosRec(raiz.dir, lista)
        lista.pop() #eliminar nó da lista após finalizar esquerda e direita

    def somarValoresCaminho(self):
        lista = []
        soma = 0
        self.__somarValoresCaminho(self.__raiz, lista,soma)

    def __somarValoresCaminho(self,raiz,lista,soma):
        if raiz is None:
            return False
            
        lista.append(raiz.info)
        soma = soma + raiz.info

        if raiz.esq is None and raiz.dir is None:
            print(lista, soma)

        else:
                
            if raiz.esq: self.__somarValoresCaminho(raiz.esq, lista,soma)
            if raiz.dir: self.__somarValoresCaminho(raiz.dir, lista,soma)
        lista.pop()

    def retornarCaminhoDeterminadaSoma(self,somadet):
        lista = []
        somacaminho = 0
        
        self.__retornarCaminhoDeterminadaSoma(self.__raiz, lista,somacaminho,somadet)

    def __retornarCaminhoDeterminadaSoma(self,raiz,lista,somacaminho,somadet):
        if raiz is None:
            return False
        
        lista.append(raiz.info)
        somacaminho += raiz.info

        if somadet == somacaminho:
            print(lista,"a soma do caminho:", somacaminho)

        else: 
            if raiz.esq: self.__retornarCaminhoDeterminadaSoma(raiz.esq, lista,somacaminho,somadet)
            if raiz.dir: self.__retornarCaminhoDeterminadaSoma(raiz.dir, lista,somacaminho,somadet)
        lista.pop()

    def retornarCaminho3(self):
        lista = []
        qtd = 0

        self.__retornarCaminho3(self.__raiz,lista,qtd)

    def __retornarCaminho3(self,raiz,lista,qtd):
        if raiz is None:
            return False
        
        lista.append(raiz.info)
        qtd += 1

        if qtd == 3:
            print(lista,"quantidade de tamanho 3")

        else:
            if raiz.esq: self.__retornarCaminho3(raiz.esq, lista,qtd)
            if raiz.dir: self.__retornarCaminho3(raiz.dir, lista,qtd)
        lista.pop()




arv = ArvBin()

arv.insere(3)
arv.insere(1)
arv.insere(2)
arv.insere(0)
arv.insere(4)
print(arv)
arv.pre_ordem()
arv.menorValor()

arv.imprimeCaminhos()
arv.somarValoresCaminho()
arv.retornarCaminhoDeterminadaSoma(7)
arv.retornarCaminho3()