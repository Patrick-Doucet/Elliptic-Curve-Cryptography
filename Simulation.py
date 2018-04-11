#Simulation of Elliptic Curve Cryptography
import PrimeGenerator
from EllipticCurve import *
import random
import math

dashString = "-"*40

def diffieHellmanExchange(curve, p):

    aNum = random.randint(0, int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16))
    print("Alan's Secret Number:\n")
    print(str(aNum) +"\n")
    
    bNum = random.randint(0, int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16))    
    print("Belle's Secret Number:\n")
    print(str(bNum) +"\n")

    print("Alan's Secret Key: Ka\n")
    Ka = p.Multiply(aNum)
    print("(" + str(Ka.x) + ", " + str(Ka.y) + ")\n")
    
    print("Belle's Secret Key: Kb\n")
    Kb = p.Multiply(bNum)
    print("(" + str(Kb.x) + ", " + str(Kb.y) + ")\n")
    
    print("Alan's Shared Secret Key with Belle: Kab\n")
    Kab = Ka.Multiply(bNum)
    print("(" + str(Kab.x) + ", " + str(Kab.y) + ")\n")
    
    print("Belle's Shared Secret Key with Alan: Kba\n")
    Kba = Kb.Multiply(aNum)
    print("(" + str(Kba.x) + ", " + str(Kba.y) + ")\n")
    
    if(Kab == Kba):
        print("Both keys are the same: Successful Key Transfer")
    else:
        print("Both keys are not the same: Unsuccessful Key Transfer")

    return Kab

def threePassProtocol(Msg, SKey):
    return

def main():

    print(dashString)
    print("Initial curve setup\n" + dashString)
    Curve = EllipticCurve(int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFF", 16), int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFC", 16), int("E87579C11079F43DD824993C2CEE5ED3", 16), int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))
    print("The curve created in this simulation is secp128r1")
    #We need to find and define our 2 first points
    Point1 = EllipticCurvePoint(6, 15, Curve)
    Point2 = EllipticCurvePoint(4, Curve.solve(4), Curve)

    print("How many points would you like to plot?")
    numOfCoords = input()
    Curve.plot(int(numOfCoords))

    print("\n" + dashString)
    print("Generating Prime Numbers...\n" + dashString)
    primeNumbers = PrimeGenerator.createPrimeNumbers(100)
    print(primeNumbers)
    #For simulation purpose, input() acts as a system pause
    input()
    print("\n" + dashString)
    print("Diffie Hellman Key Exchange\n" + dashString)
    SecretKey = diffieHellmanExchange(Curve, Point1)
    input()
    print(dashString)
    print("Message encryption and decryption process\n" + dashString)
    message = ""
    print("Alan:\n")
    message = input("What string would you like to send?\n")
    
    while len(message) > 16:
        message = input("Message too long, please choose another message to encrypt\n")

    print("\nSending: " + message + " to Belle")

    print(dashString + "\n")

    print("Executing ThreePassProtocol...\n")

    threePassProtocol(message, SecretKey)

    print(dashString + "\n" + dashString + "\nEnd of message exchange")



if __name__ == "__main__":
    main()
