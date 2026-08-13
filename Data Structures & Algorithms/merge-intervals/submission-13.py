class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in intervals:
            if i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],i[1])
            else:
                result.append(i)
        return result
                       