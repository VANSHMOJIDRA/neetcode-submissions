class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!= 0:
            check = (a ^ b)
            carry = ( a & b) << 1
            a = check & 0xFFFFFFFF
            b = carry & 0xFFFFFFFF
        if a >= 2**31:
            a = a - 2**32
        return a        