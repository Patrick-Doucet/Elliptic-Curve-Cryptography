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
        m = float((point2.y-point1.y)/(point2.x - point1.x))
        mBPair = (m, float((point1.y - (m*point1.x))))
        return mBPair

    #Calculate the m and b of the Tangent line
    def Tangent(self, point):
        m = ((3 * (point.x**2) + self.a) / (2*point.y))
        mBPair = (m, float((point.y - (m*point.x))))
        return mBPair

    def solve(self, x):
        return math.sqrt(x**3 + self.a*x + self.b)

    def linear(self, x, m, b):
        return (m*x + b) % float(340282366920938463463374607431768211456)

class EllipticCurvePoint(EllipticCurve):

    #When creating a point, we have to give which curve it belongs to
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    #Overloading addition operator
    def __add__(self, other):
        pairMB = tuple()
        if self != other:
            pairMB = EllipticCurve.Secant(self.curve, self, other)
        if self == other:
            pairMB = EllipticCurve.Tangent(self.curve,self)
        if (self.x == 0 and self.y == 0) and (other.x != 0 and other.y != 0):
            return other
        if (self.x != 0 and self.y != 0) and (other.x == 0 and other.y == 0):
            return self
        print("Pair")
        print(pairMB)
        #Now that we have our m and b, we have our y = mx + b equation
        #We now have to find the next point in which this line intersects on the elliptic curve
        point = EllipticCurvePoint(0,0, self.curve)
        intersections = fsolve(lambda x: self.curve.linear(x, pairMB[0], pairMB[1]) - self.curve.solve(x), 0)
        print("Intersections")
        print(intersections)
        point.x = (intersections[0]) % float(340282366920938463463374607431768211456)
        point.y = (point.curve.solve(point.x)) % float(340282366920938463463374607431768211456)

        #for i in intersections:
        #    if i != self.x and i != other.x:
        #        point.x = intersections[0]
        #        point.y = point.curve.solve(point.x)
        print(point.x)
        print(point.y)
        return point
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.curve != other.curve
    #We redefine the multiplication of 2 points to use the square and multiply method
    #def __rmul__(self, other):
    #    tempPoint = other
    #    for i in range(1, self):
    #        tempPoint = tempPoint + tempPoint
    #    return tempPoint

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
            input()
            if i == 0:
                tempPoint = tempPoint + tempPoint
            else:
                tempPoint = tempPoint + tempPoint 
                print(tempPoint.x, tempPoint.y)
                tempPoint = tempPoint + PPoint
        return tempPoint

