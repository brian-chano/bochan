isPrime :: Int -> Bool
isPrime n = length [x | x <- [1..n], n `mod` x ==0] == 2

sieveList xs 	| null xs	= []
				| otherwise	= [y] ++ sieveList([x | x <-xs, x `mod` y /= 0])
				where
					y = head xs
primeFactors :: Int -> [Int]
primeFactors n = [x | x <- [2..n], isPrime x]