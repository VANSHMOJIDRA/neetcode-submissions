class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            can = (nums[i],current_max * nums[i],current_min * nums[i])
            new_max = max(can)
            new_min = min(can)
            current_max = new_max
            current_min = new_min
            result = max(result,current_max)
        return result

        