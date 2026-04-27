class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = sorted(s)
        countt = sorted(t)

        return counts == countt