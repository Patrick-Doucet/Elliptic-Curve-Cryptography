#Simulation of Elliptic Curve Cryptography
import PrimeGenerator
from EllipticCurve import *
import random
import math

dashString = "-"*40

def diffieHellmanExchange(curve):
    #Do the exchange, store in variables for the prints
    xNum = random.randint(0, 1000000)
    print(xNum)
    yNum = curve.solve(xNum)
    print(yNum)
    publicPoint = EllipticCurvePoint(xNum, yNum, curve)
    print("Generated public point: (" + str(publicPoint.x) + ", " + str(publicPoint.y) + ")")
    #print Ka, then Kab, then Kba, then Kb
    
    return

def threePassProtocol():
    return

def main():

    print("Initial curve setup\n" + dashString)
    Curve = EllipticCurve(int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFF", 16), int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFC", 16), int("E87579C11079F43DD824993C2CEE5ED3", 16), int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))
    print("The curve created in this simulation is secp128r1")
    #We need to find and define our 2 first points
    Point1 = EllipticCurvePoint(2,3, Curve)
    Point2 = EllipticCurvePoint(4,5, Curve)
    point3 = Point1.Multiply(2)
    print("How many points would you like to plot?")
    numOfCoords = input()
    Curve.plot(int(numOfCoords))

    print("\nGenerating Prime Numbers...\n" + dashString)
    primeNumbers = PrimeGenerator.createPrimeNumbers(100)
    print(primeNumbers)
    #For simulation purpose, input() acts as a system pause
    input()

    print("Diffie Hellman Key Exchange\n" + dashString)
    diffieHellmanExchange(Curve)
    input()

    print("Message encryption and decryption process\n" + dashString)
    message = ""
    print("Alan:\n")
    message = input("What string would you like to send?\n")
    
    while len(message) > 16:
        message = input("Message too long, please choose another message to encrypt\n")

    print("\nSending: " + message + " to Belle")


if __name__ == "__main__":
    main()
