def gerarListaValoresAleatorios(quantidade):
   from random import randint
   resposta = []
   for i in range(quantidade):
       resposta.append(randint(0,1000))
   return resposta

def bubbleSort(lista):
    cont = 0
    for passnum in range(len(lista)-1,0,-1):
        troca1 = False
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                troca(lista,i)
                troca1 = True
                cont +=1

        if troca1 == False:
            break
    print(cont)

def troca(lista,i):
    temp = lista[i]
    lista[i] = lista[i+1]
    lista[i+1] = temp

def tempo(lista):
    import time
    lista = gerarListaValoresAleatorios(255555)
    inicio = time.time()
    bubbleSort(lista)
    fim = time.time()
    tempo = fim-inicio
    print(f'A função demorou {tempo:.5f} segundos')



def ordena():
    lista = gerarListaValoresAleatorios(20)
    print(lista)
    bubbleSort(lista)
    print(lista)

import time
lista = gerarListaValoresAleatorios(255555)
inicio = time.time()
bubbleSort(lista)
fim = time.time()
tempo = fim-inicio
print(f'A função demorou {tempo:.5f} segundos')