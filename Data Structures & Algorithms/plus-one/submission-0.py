class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strify = "".join([str(i) for i in digits])
        intermediate = int(strify) + 1
        digitlist = [int(num) for num in str(intermediate)]
        return digitlist