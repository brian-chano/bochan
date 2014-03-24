'''
Project Euler
---------------
Question 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer: 6857
'''

import math

def compute(upper_limit): # Upper limit is not included in the range
	return sum(set([x for x in range(3,upper_limit) if x % 3 == 0 or x % 5 == 0]))

if __name__ == '__main__':
        upper_limit = input("What is your upper limit? ")
        arr = [x for x in range(2, upper_limit+1)]

        for i in range(0, upper_limit):
                if(arr[i] == arr[len(arr)-1]):
                        break
        else:
                for j in arr:
                        if(j % arr[i] == 0):
                                arr.pop()
        print arr    
                       
    
