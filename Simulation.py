#Simulation of Elliptic Curve Cryptography
import PrimeGenerator
from EllipticCurve import *

dashString = "-"*40

def diffieHellmanExchange():
    #Do the exchange, store in variables for the prints

    #print Ka, then Kab, then Kba, then Kb
    
    return


def threePassProtocol():
    return

def main():

    print("Initial curve setup")
    Curve = EllipticCurve(int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFF", 16), int("FFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFC", 16), int("E87579C11079F43DD824993C2CEE5ED3", 16), int("03161FF7528B899B2D0C28607CA52C5B86" ,16), int("FFFFFFFE0000000075A30D1B9038A115", 16), int("01", 16))
    print("The curve created in this simulation is secp128r1")
    
    print("How many points would you like to plot?")
    numOfCoords = input()
    #Curve.plot(int(numOfCoords))

    print("Generating Prime Numbers...")
    primeNumbers = PrimeGenerator.createPrimeNumbers(1000000)
    print(primeNumbers)
    input()

    print("Diffie Hellman Key Exchange\n" + dashString)
    diffieHellmanExchange()
    #For simulation purpose, input() acts as a system pause
    input()

    input()
    message = ""
    print("Alan:")
    print(dashString)
    message = input("What string would you like to send?\n")
    
    while len(message) > 16:
        message = input("Message too long, please choose another message to encrypt\n")

    print("Sending: " + message + " to Belle")


if __name__ == "__main__":
    main()
