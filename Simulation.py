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

    #Alan's secret key is the multiplication of the point p and Alan's Secret Number
    print("Alan's Secret Key: Ka\n")
    Ka = p.Multiply(aNum)
    print("(" + str(Ka.x) + ", " + str(Ka.y) + ")\n")
    
    #Belle's secret key is the multiplication of the point p and Belle's Secret Number
    print("Belle's Secret Key: Kb\n")
    Kb = p.Multiply(bNum)
    print("(" + str(Kb.x) + ", " + str(Kb.y) + ")\n")
    
    #Alan transfers the Ka Key to Belle, which she then multiplies it with her Secret Number
    print("Alan's Shared Secret Key with Belle: Kab\n")
    Kab = Ka.Multiply(bNum)
    print("(" + str(Kab.x) + ", " + str(Kab.y) + ")\n")
    
    #In parallel, Belle transfers the Kb Key to Alan, which he then multiplies it with his Secret Number
    print("Belle's Shared Secret Key with Alan: Kba\n")
    Kba = Kb.Multiply(aNum)
    print("(" + str(Kba.x) + ", " + str(Kba.y) + ")\n")

    #If Kab is equal to Kba, the key sharing was a success 
    if(Kab == Kba):
        print("Both keys are the same: Successful Key Transfer")
    else:
        print("Both keys are not the same: Unsuccessful Key Transfer")

    return Kab

#Uses our point P to demonstrate that if we can encrypt our message into a point, we can successfully encrypt and decrypt this point
def threePassProtocol(P):
    
    print("Initial point P:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")

    #Multiply Alan's Secret key to the point
    print("Encrypting point with Alan's Secret Key...\n")
    P = P.Multiply(aNum)
    print("Send point Pa to Belle:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    
    #Multiply Belle's Secret key to the point
    print("Encrypting point with Belle's Secret Key...\n")
    P = P.Multiply(bNum)
    print("Send point Pab to Alan:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")

    #Inverse Multiply Alan's Secret key to the point
    print("Decrypting point with Alan's Secret Key...\n")
    P = P.Multiply(P.inv_mod(aNum))
    print ("Send point Pb to Belle:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")
    
    #Inverse Multiply Alan's Secret key to the point
    print("Decrypting point with Belle's Secret Key...\n")
    P = P.Multiply(P.inv_mod(bNum))
    print ("Final decrypted point P:\n")
    print("(" + str(P.x) + ", " + str(P.y) + ")\n")

    return

def main():

    #Create the standard curve secp128r1 using the EllipticCurve class
    print(dashString)
    print("Initial curve setup\n" + dashString)
    Curve = EllipticCurve(int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFF", 16), int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFC", 16), int("E87579C11079F43DD824993C2CEE5ED3", 16), int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))
    print("The curve created in this simulation is secp128r1")
    
    #Create a point which is a generator to the ellipic curve
    Point1 = EllipticCurvePoint(6, 15, Curve)

    #Plot out the positive portion of the curve (Due to the formula being implicit)
    print("How many points would you like to plot?")
    numOfCoords = input()
    Curve.plot(int(numOfCoords))
    print(dashString)
    print(dashString)

    #For simulation purposes, input() acts as a system pause
    input()
    print("\n" + dashString)

    #Calls the diffieHellmanExchange with our created curve and point
    print("Diffie Hellman Key Exchange\n" + dashString)
    SecretKey = diffieHellmanExchange(Curve, Point1)
    input()
    print(dashString)
    print(dashString + "\n")
    print("\n" + dashString)

    #Calls threePassProtocol to show the secure transfer of a point
    print("Executing ThreePassProtocol...")
    print(dashString + "\n")
    threePassProtocol(Point1)

    print(dashString + "\n" + dashString + "\nEnd of message exchange")



if __name__ == "__main__":
    main()
