class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        sorted_s = Counter(s)
        sorted_t = Counter(t)

        return sorted_s == sorted_t