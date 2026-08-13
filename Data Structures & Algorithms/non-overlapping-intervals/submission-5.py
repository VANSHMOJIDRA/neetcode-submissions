class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < prev_end:
                prev_end = min(prev_end,i[1])
                count += 1
            else:
                prev_end = i[1]
        return count