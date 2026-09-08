def helper(num: int) -> int:
    """
    Return the sum of squares of the numbers digits
    """
    squared = 0
    for digit in str(num):
        squared += int(digit) ** 2
    return squared

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        happy = helper(n)

        if happy == 1:
            return True

        while happy != 1:
            if happy in seen:
                return False
            seen.add(happy)
            happy = helper(happy)
        return True
