# Given an integer n, return the number of prime numbers that are strictly less than n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for number in range(2, int(math.sqrt(n)) + 1):
            if is_prime[number]:

                # This loop marks all the multiples of choosen number as false
                for i in range(number**2, n, number):
                    is_prime[i] = False

        return(sum(is_prime))
