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
        m = ((3 * (point.x**2) + self.a)) / 2
        b = math.sqrt(self.b)
        mBPair = (m, b)
        return mBPair

    def solve(self, x):
        return math.sqrt(x**3 + self.a*x + self.b)

class EllipticCurvePoint(EllipticCurve):

    #When creating a point, we have to give which curve it belongs to
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    #Overloading addition operator
    def __add__(self, other):
        
        pairMB = tuple()
        if self != other and self != 0 and other != 0:
            pairMB = EllipticCurve.Secant(self.curve, self, other)
        if self == other:
            pairMB = EllipticCurve.Tangent(self.curve,self)
        if self == 0 and other != 0:
            pairMB = EllipticCurve.Tangent(self.curve,other)
        if self != 0 and other == 0:
            pairMB = EllipticCurve.Tangent(self.curve,self)
        
        #Now that we have our m and b, we have our y = mx + b equation
        #We now have to find the next point in which this line intersects on the elliptic curve

        return
    
    #We redefine the multiplication of 2 points to use the square and multiply method
    #def __rmul__(self, other):
    #    tempPoint = other
    #    for i in range(1, self):
    #        tempPoint = tempPoint + tempPoint
    #    return tempPoint

    #We redefine the multiplication of a point and a scalar to use the square and multiply method
    def __mul__(self, other):
        #Convert the scalar to a binary value
        binString = []
        scalar = self
        while scalar != 0:
            binString.append(scalar%2)
            scalar = scalar / 2
        tempPoint = other
        binString.reverse()
        #Square multiply algorithm
        for i in binString:
            if i == 0:
                tempPoint = tempPoint + tempPoint
            else:
                tempPoint = tempPoint + tempPoint + other
        return tempPoint

