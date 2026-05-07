class Solution:
    def combinationSum(self,nums:list[list[int]] , target:int) -> list[list[int]]:
        result = []
        def solve(i,cc,cs):
            if cs ==  target:
                result.append(cc.copy())
                return 
            if cs > target:
                return
            for num in range(i,len(nums)):
                cc.append(nums[num])
                solve(num,cc,cs + nums[num])
                cc.pop()
        solve(0,[],0)
        return result