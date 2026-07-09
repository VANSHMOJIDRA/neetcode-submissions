class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1+amount] * (1+amount)
        dp[0] = 0
        for i in range(1,1+amount):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i],1 + dp[i-c])
        return dp[amount] if dp[amount] != 1 + amount else -1

        