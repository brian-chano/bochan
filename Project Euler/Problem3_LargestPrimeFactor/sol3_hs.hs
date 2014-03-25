{--
Project Euler
---------------
Question 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer: 6857
--}

isPrime :: Int -> Bool
isPrime n = length [x | x <- [1..n], n `mod` x ==0] == 2

sieveList xs 	| null xs	= []
				| otherwise	= [y] ++ sieveList([x | x <-xs, x `mod` y /= 0])
				where
					y = head xs
primeFactors :: Int -> [Int]
primeFactors n = [x | x <- [2..n], n `mod` x == 0, isPrime x]

largestPrime = head . primeFactors