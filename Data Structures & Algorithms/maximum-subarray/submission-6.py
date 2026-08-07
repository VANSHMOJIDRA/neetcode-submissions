class Solution:
    def maxSubArray(self,nums:list[int]) -> int:
        curr = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr = curr + nums[i]
            max_sum = max(max_sum,curr)
        return max_sum