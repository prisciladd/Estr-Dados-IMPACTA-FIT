import math

class Ponto:

    def __init__(self):
        self.x = 0
        self.y = 0
   
    def obter_coordenadas(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
   
    def igual(self, p):
        return (self.x == p.x) and (self.y == p.y)

    def distancia(self,p):
        self.p = p
        d = math.sqrt((self.x - p.x )**2 + (self.y - p.y )**2) #(3**2= 9) + (4**2= 16) --> 9+16 = 25 sqrt(25)= 5  
        return d

    def transladar (self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.x = self.dx
        self.y = self.dy

pt1 = Ponto()
pt1.obter_coordenadas()
print(pt1.x)
print(pt1.y)

pt2 = Ponto()
pt2.x=3
pt2.y=4
pt2.obter_coordenadas()
print(pt2.x)
print(pt2.y)

print(pt1.igual(pt2))

print (pt1.distancia(pt2))

pt2.transladar(5,6)

print(pt2.x)
print(pt2.y)