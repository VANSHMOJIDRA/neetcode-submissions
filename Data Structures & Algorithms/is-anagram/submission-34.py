class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        if len(s) != len(t):
            return False
        counts,countt = {},{}
        for n in range(len(s)):
            counts[s[n]] = 1 + counts.get(s[n],0)
            countt[t[n]] = 1 + countt.get(t[n],0)
        return counts == countt