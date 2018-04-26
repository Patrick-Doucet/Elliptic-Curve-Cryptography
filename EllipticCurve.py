#Elliptic Curve Class
import matplotlib.pyplot as plt
import math
from numpy import arange
from numpy import meshgrid

class EllipticCurve:

    #Parameters needed to create the EllipticCurve
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

class EllipticCurvePoint(EllipticCurve):

    #When creating a point, the curve it belongs to is given
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    #Overloading addition operator
    def __add__(self, other):

        #To ensure the commutativity of the addition
        if self.x < other.x:
            a = self
            b = other
        else:
            a = other
            b = self

        #The various cases in which the 2 points may present
        #Point1 = (0,0), return Point2
        if (a.x == 0 and a.y == 0):
            return b
        #Point2 = (0,0), return Point1
        elif (b.x == 0 and b.y == 0):
            return a
        #Point1 = inverse(Point2), return (0,0)
        elif b == a.ec_inv():
            return EllipticCurvePoint(0,0,a.curve)
        #The general case
        else:
            #Tangent to find third point
            if a == b:
                m = (3 * (a.x**2) + a.curve.a) * a.inv_mod(2*a.y)
            #Secant to find third point
            else:
                m = (b.y-a.y) * a.inv_mod(b.x - a.x)
        point = EllipticCurvePoint(0,0,a.curve)
        
        #Solving the new 3rd point that intersects with the curve
        point.x = ((m**2 % a.curve.p) - a.x - b.x) % a.curve.p
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
    
    #Defining the == Operator between 2 EllipticCurvePoints
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    #Defining the != Operator between 2 EllipticCurvePoints
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.curve != other.curve

    #Redefine the multiplication of a point and a scalar to use the square and multiply method
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
        for i in binString:
            if i == 0:
                tempPoint = tempPoint + tempPoint
                tempPoint.x = tempPoint.x % self.curve.p
                tempPoint.y = tempPoint.y % self.curve.p
            else:
                tempPoint = tempPoint + tempPoint
                tempPoint.x = tempPoint.x % self.curve.p
                tempPoint.y = tempPoint.y % self.curve.p
                tempPoint = tempPoint + PPoint
                tempPoint.x = tempPoint.x % self.curve.p
                tempPoint.y = tempPoint.y % self.curve.p
        return tempPoint
