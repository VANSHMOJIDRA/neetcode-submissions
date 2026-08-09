class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        ins = False
        for i in intervals:
            if ins == True:
                result.append(i)
            elif i[1] < newInterval[0]:
                result.append(i)
            elif i[0] > newInterval[1]:
                result.append(newInterval)
                result.append(i)
                ins = True
            else:
                m1 = min(i[0],newInterval[0])
                m2 = max(i[1],newInterval[1])
                newInterval = [m1,m2]
        if not ins:
            result.append(newInterval)
        return result