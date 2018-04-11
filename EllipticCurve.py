#Elliptic Curve Class
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

class EllipticCurve:

    def __init__(self, p, a, b, G, n, h):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
    
    #Plot the elliptic curve with n points
    def plot(self, n):
        xList= list()
        yList= list()

        for i in range(0, n):
            xList.append(i)
            yList.append(math.sqrt(i**3 + self.a*i + self.b))
        plt.plot(xList, yList)
        plt.show()

    def solve(self, x):
        return math.sqrt(x**3 + self.a*x + self.b)

    def linear(self, x, m, b):
        return (m*x + b) % self.p

class EllipticCurvePoint(EllipticCurve):

    #When creating a point, we have to give which curve it belongs to
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    #Overloading addition operator
    def __add__(self, other):

        if self.x < other.x:
            a = self
            b = other
        else:
            a = other
            b = self

        if (a.x == 0 and a.y == 0):
            return b
        elif (b.x == 0 and b.y == 0):
            return a
        elif b == a.ec_inv():
            return EllipticCurvePoint(0,0,a.curve)
        else:
            if a == b:
                m = (3 * (a.x**2) + a.curve.a) * a.inv_mod(2*a.y)
            else:
                m = (b.y-a.y) * a.inv_mod(b.x - a.x)
        point = EllipticCurvePoint(0,0,a.curve)
            
        point.x = (m**2 - a.x - b.x) % a.curve.p
        point.y = (m*(a.x - point.x) - a.y) % a.curve.p
                
        return point

    #Inverse modulo
    def inv_mod(self, x):
        return pow(int(x), self.curve.p-2, self.curve.p)

    #Inverse of a point
    def ec_inv(self):
        if self.x == 0 and self.y == 0:
            return self
        return EllipticCurvePoint(self.x, (-self.y) % self.curve.p, self.curve)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.curve != other.curve

    #We redefine the multiplication of a point and a scalar to use the square and multiply method
    
    def Multiply(self, a):
        #Convert the scalar to a binary value
        binString = []
        scalar = a
        while scalar != 0:
            binString.append(scalar%2)
            scalar = scalar // 2
        tempPoint = EllipticCurvePoint(self.x, self.y, self.curve)
        PPoint = EllipticCurvePoint(self.x, self.y, self.curve)
        binString.pop()
        binString.reverse()
        #Square multiply algorithm
        #print(binString)
        for i in binString:
            if i == 0:
                tempPoint = tempPoint + tempPoint
            else:
                tempPoint = tempPoint + tempPoint 
                tempPoint = tempPoint + PPoint
        return tempPoint
