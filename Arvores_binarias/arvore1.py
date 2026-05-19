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


arv = ArvBin()
raiz = NO(10)
raiz.info = 80
raiz.esq = NO(34)
raiz.dir = NO(89)
raiz.esq.esq = NO(45)
raiz.esq.dir = NO(50)
raiz.dir.esq = NO(65)
raiz.dir.dir = NO(44)
raiz.dir.esq.esq = NO(5)
arv.insere(25)
arv.insere(12)
arv.insere(9)
print(raiz.info)
print(arv)
arv.pre_ordem()