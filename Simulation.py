#Simulation of Elliptic Curve Cryptography
import PrimeGenerator
from EllipticCurve import *
import random
import math

dashString = "-"*40
aNum = random.randint(0, int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16))
bNum = random.randint(0, int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16))    

def diffieHellmanExchange(curve, p):

    print("Alan's Secret Number:\n")
    print(str(aNum) +"\n")
    
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

def threePassProtocol(P):
    #We use our point P to demonstrate that we if we can encrypt our message into a point, we can successfully encrypt and decrypt this point
    print("Initial point P:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    print("Encrypting point with Alan's Secret Key...\n")
    P = P.Multiply(aNum)
    print("Send point Pa to Belle:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    print("Encrypting point with Belle's Secret Key...\n")
    P = P.Multiply(bNum)
    print("Send point Pab to Alan:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    print("Decrypting point with Alan's Secret Key...\n")
    P = P.Multiply(P.inv_mod(aNum))
    print ("Send point Pb to Belle:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    P = P.Multiply(P.inv_mod(bNum))
    print("Decrypting point with Belle's Secret Key...\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")

    return

def main():

    print(dashString)
    print("Initial curve setup\n" + dashString)
    #Curve = EllipticCurve(int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFF", 16), int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFC", 16), int("E87579C11079F43DD824993C2CEE5ED3", 16), int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))
    Curve = EllipticCurve(15733, 1, 3, int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))    
    print("The curve created in this simulation is secp128r1")
    #We need to find and define our 2 first points
    Point1 = EllipticCurvePoint(6, 15, Curve)
    point = Point1.Multiply(2).Multiply(3).Multiply(Point1.inv_mod(2)).Multiply(Point1.inv_mod(3))
    poiz = Point1.inv_mod(2)
    print(poiz)
    print(str(point.x) + "," + str(point.y))
    print("How many points would you like to plot?")
    numOfCoords = input()
    Curve.plot(int(numOfCoords))
    print(dashString)
    print(dashString)

    #print("\n" + dashString)
    #print("Generating Prime Numbers...\n" + dashString)
    #primeNumbers = PrimeGenerator.createPrimeNumbers(100)
    #print(primeNumbers)
    #For simulation purpose, input() acts as a system pause
    input()
    print("\n" + dashString)
    print("Diffie Hellman Key Exchange\n" + dashString)
    SecretKey = diffieHellmanExchange(Curve, Point1)
    input()
    print(dashString)
    #print("Message encryption and decryption process\n" + dashString)
    #message = ""
    #print("Alan:\n")
    #message = input("What string would you like to send?\n")
    # 
    #while len(message) > 16:
    #    message = input("Message too long, please choose another message to encrypt\n")

    #print("\nSending: " + message + " to Belle")

    print(dashString + "\n")

    print("\n" + dashString)
    print("Executing ThreePassProtocol...")
    print(dashString + "\n")
    threePassProtocol(Point1)

    print(dashString + "\n" + dashString + "\nEnd of message exchange")



if __name__ == "__main__":
    main()
