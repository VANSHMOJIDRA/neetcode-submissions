class Solution:
    def missingNumber(self,nums:list[int]) -> int:
        n = len(nums)
        res = 0
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        res = expected_sum - actual_sum
        return res