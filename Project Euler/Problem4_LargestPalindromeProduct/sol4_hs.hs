{--
Project Euler
---------------
Problem 4:
A palindrome number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
--}

palindrome :: String -> Bool
palindrome xs = all (\(x,y) -> x == y) $ zip (take n xs) (take n (reverse xs))
				where
					n = length xs

ans = maximum $ filter (\x -> palindrome . show $ x) [(i*j) | i <- [100..999], j <- [i, 999]]