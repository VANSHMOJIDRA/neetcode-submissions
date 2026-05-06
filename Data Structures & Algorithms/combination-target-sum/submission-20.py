class Solution:
    def combinationSum(self,nums:list[int],target:int) -> list[list[int]]:
        result = []

        def solve(i,c_c,c_s):
            if c_s == target:
                result.append(c_c.copy())
                return
            if c_s >= target:
                return
            
            for i in range(i,len(nums)):
                c_c.append(nums[i])
                solve(i,c_c,c_s + nums[i])
                c_c.pop()
        solve(0,[],0)
        return result