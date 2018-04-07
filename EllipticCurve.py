#Elliptic Curve Class
import matplotlib.pyplot as plt
import math
class EllipticCurve:

    def __init__(self, p, a, b, G, n, h):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
    
    def plot(self):
        xList= list()
        yList= list()

        for i in range(0, 10000000):
            xList.append(i)
            yList.append(math.sqrt(i**3 + self.a*i + self.b))
        plt.plot(xList, yList)
        plt.show()

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
