'''
Project Euler
---------------
Problem 4:
A palindrome number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
'''

def palindrome(prod):
	str_prod = str(prod)
	i,j = 0, len(str_prod) - 1
	
	while not (i > j):
		if str_prod[i] != str_prod[j]:
			return False
		i, j = i+1, j-1
	
	return True

largest_palindrome, first_number, upper_boundary = 0, 100, 1000
for i in range(first_number, upper_boundary):
	for j in range(first_number,i):
		prod = i * j
		if palindrome(prod) and prod > largest_palindrome:
			largest_palindrome = prod


print largest_palindrome
