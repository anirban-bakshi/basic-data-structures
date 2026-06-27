# general way to calculate the no of ways for a die roll to add up to a given number, climibing steps 1,2,3 steps at a time

from typing import List

class GeneralWays:

    def ways(self, n:int, steps:List[int]):

        if n<0:
            return 0
        
        if n == 0:
            return 1
        
        # initialize a dp array
        dp = [0] * (n+1)
        dp[0] = 1 # base case

        for i in range (1, n+1):
            for s in steps:
                if i - s >= 0:
                    dp[i] += dp[i-s]

        
        return dp[n]

