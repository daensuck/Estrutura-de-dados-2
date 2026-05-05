import math

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def mover(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distancia(self, outro_ponto):
        return math.sqrt((self.__x - outro_ponto.__x)**2 + (self.__y - outro_ponto.__y)**2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"

x1 = int(input("Digite a coordenada x do primeiro ponto: "))
y1 = int(input("Digite a coordenada y do primeiro ponto: "))
x2 = int(input("Digite a coordenada x do segundo ponto: "))
y2 = int(input("Digite a coordenada y do segundo ponto: "))

p1 = Ponto(x1, y1)
p2 = Ponto(x2, y2)

print("Distância entre os pontos:", p1.distancia(p2))

p1.mover(2, 3)
print("Coordenadas do primeiro ponto após mover:", p1)