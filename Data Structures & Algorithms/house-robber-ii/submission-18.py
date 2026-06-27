class Solution:
    def rob(self,nums:list[int])-> int:
        if len(nums) == 1:
            return nums[0]
        def helper(h):
            if len(h) == 1:
                return h[0]
            dp = [0] * len(h)
            dp[0] = h[0]
            dp[1] = max(h[0],h[1])
            for i in range(2,len(h)):
                dp[i] = max(h[i] + dp[i-2], dp[i-1])
            return dp[-1]
        return max(helper(nums[0:len(nums)-1]) , helper(nums[1:len(nums)]))