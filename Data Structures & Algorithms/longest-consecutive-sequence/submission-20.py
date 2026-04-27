class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        res = set(nums)
        for n in res:
            if (n-1) not in res:
                length = 1
                while (n + length) in res:
                    length += 1
                longest = max(length,longest)
        return longest