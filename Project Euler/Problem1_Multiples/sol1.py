'''
Project Euler
---------------
Question 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
'''

import math

def compute(upper_limit): # Upper limit is not included in the range
	return sum(set([x for x in range(3,upper_limit) if x % 3 == 0 or x % 5 == 0]))

if __name__ == '__main__':
    upper_limit = input("What is your upper limit? ")
    print compute(upper_limit)
