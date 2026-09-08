class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        result = 1
        for i in range(1, x + 1):
            if i * i > x:
                return result
            result = i
        return result