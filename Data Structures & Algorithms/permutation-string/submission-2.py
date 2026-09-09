class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = {}
        for char in s1:
            map1[char] = map1.get(char, 0) + 1
        map2 = {}
        for i in range(len(s1)):
            map2[s2[i]] = map2.get(s2[i], 0) + 1

        if map1 == map2:
            return True
        for right in range(len(s1), len(s2)):
            map2[s2[right]] = map2.get(s2[right], 0) + 1

            leftChar = s2[right - len(s1)]
            map2[leftChar] -= 1
            if map2[leftChar] == 0:
                del map2[leftChar]
            if map1 == map2:
                return True
        return False