class Solution:
    def maxProduct(self,nums:list[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            can = (nums[i],current_max * nums[i],current_min * nums[i])
            max_new = max(can)
            min_new = min(can)
            current_max = max_new
            current_min = min_new
            result = max(result,current_max)
        return result
