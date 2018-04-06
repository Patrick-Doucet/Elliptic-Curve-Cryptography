#Elliptic Curve Class
class EllipticCurve:

    def __init__(self, p, a, b, G, n, h):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
    

    
    def Secant(self, point1, point2):
        return

    def Tangent(self, point):
        return

class Point(EllipticCurve):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        #Don't delete this

        #if self != other and self != 0 and other != 0:
            #Secant(self, other)
        #if self == other:
            #Tangent(self)
        #if self == 0 and other != 0:
            #Tangent(other)
        #if self != 0 and other == 0:
            #Tangent(self)
        
        return
