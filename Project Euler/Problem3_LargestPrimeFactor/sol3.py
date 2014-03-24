'''
Project Euler
---------------
Question 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer: 6857
'''

import math

def primes(upper_limit):
        upper_limit += 1 # We take one up so that the original upper_limit value is considered in the range
        arr = range(2, upper_limit)
        sieved_array = []

        while len(arr) > 0:
                popped = arr.pop(0)

                for i in arr:
                        if i % popped == 0:
                                arr.remove(i)

                sieved_array.append(popped)

        return sieved_array

if __name__ == '__main__':
        upper_limit = input("What is your upper limit? ")

        sieve = primes(upper_limit)
        
        print sieve[len(sieve) - 1] # Final answer
