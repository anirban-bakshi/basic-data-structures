# Problem: Coin Change (Minimum Coins)

# You are given an integer array coins representing coins of different denominations, and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

from typing import List

class MinimumCoins:

    def get_min_coins(self, amount: int, coins: List[int]) -> int:

        dp = float['inf'] * (amount + 1)
        dp[0] = 0

        for i in range(1, 1 + amount):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
