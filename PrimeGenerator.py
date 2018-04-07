#Script to generate subgroup of prime numbers
import math

def createPrimeNumbers(n):
    #Give the initial prime numbers of 
    primeNumbers = list()
    primeNumbers.append(int(2))
    for i in range(3, n, 2):
        isPrime = True
        for j in range(3, int(math.sqrt(i)), 2):
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            primeNumbers.append(i)

    return primeNumbers

