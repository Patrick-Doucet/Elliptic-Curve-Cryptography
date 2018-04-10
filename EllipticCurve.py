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

    #Calculate the m and b of the Secant line
    def Secant(self, point1, point2):
        print("Secant")
        m = float((point2.y-point1.y)/(point2.x - point1.x))
        mBPair = (m, float((point2.y - (m*point2.x))))
        return mBPair

    #Calculate the m and b of the Tangent line
    def Tangent(self, point):
        print("Tangent")
        if point.y != 0:
            m = ((3 * (point.x**2) + self.a) / (2*point.y))
        else:
            m = 0
        mBPair = (m, float((point.y - (m*point.x))))

        return mBPair

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

    def __add__(self, other):

        if (self.x == 0 and self.y == 0):
            return other
        elif (other.x == 0 and other.y == 0):
            return self
        elif other == self.ec_inv():
            return EllipticCurvePoint(0,0,self.curve)
        else:
            if self == other:
                m = float((3 * (self.x**2) + self.curve.a) * self.inv_mod(2*self.y))
            else:
                m = float((other.y-self.y) * self.inv_mod(other.x - self.x))
        point = EllipticCurvePoint(0,0,self.curve)
        point.x = (m**2 - self.x - other.x) % self.curve.p
        point.y = (m*(self.x - point.x) - self.y) % self.curve.p
        return point

    #Inverse modulo
    def inv_mod(self, x):
        return pow(int(x), self.curve.p-2, self.curve.p)

    #Inverse of a point
    def ec_inv(self):
        if self.x == 0 and self.y == 0:
            return self
        return EllipticCurvePoint(self.x, (-self.y) % self.curve.p, self.curve)

    #Overloading addition operator
    #def __add__(self, other):
        #pairMB = tuple()
        #if self != other:
        #    pairMB = EllipticCurve.Secant(self.curve, self, other)
        #if self == other:
        #    pairMB = EllipticCurve.Tangent(self.curve,self)
        #if (self.x == 0 and self.y == 0) and (other.x != 0 and other.y != 0):
        #    return other
        #if (self.x != 0 and self.y != 0) and (other.x == 0 and other.y == 0):
        #    return self
        #print("Pair")
        #print(pairMB)
        #Now that we have our m and b, we have our y = mx + b equation
        #We now have to find the next point in which this line intersects on the elliptic curve
        #point = EllipticCurvePoint(0,0, self.curve)
        #point.x = pairMB[0]**2 - self.x - other.x
        #point.y = pairMB[0]*(self.x - point.x) - self.y
        #if pairMB[0] == 0 and pairMB[1] == 0:
        #    point.x = self.x
        #    point.y = self.y
        #print("POINTS")
        #return point
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.curve != other.curve

    #We redefine the multiplication of a point and a scalar to use the square and multiply method
    def Multiply(self, a):
        print("Multiplying")
        #Convert the scalar to a binary value
        binString = []
        scalar = a
        while scalar != 0:
            binString.append(scalar%2)
            scalar = scalar // 2
        tempPoint = EllipticCurvePoint(self.x, self.y, self.curve)
        PPoint = EllipticCurvePoint(self.x, self.y, self.curve)
        binString.reverse()
        #Square multiply algorithm
        print(binString)
        for i in binString:
            if i == 0:
                tempPoint = tempPoint + tempPoint
                print(tempPoint.x, tempPoint.y)
            else:
                tempPoint = tempPoint + tempPoint 
                print(tempPoint.x, tempPoint.y)
                tempPoint = tempPoint + PPoint
                print(tempPoint.x, tempPoint.y)
        return tempPoint

