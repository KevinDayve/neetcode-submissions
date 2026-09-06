class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Container = {}
        for char in s:
            Container[char] = Container.get(char, 0) + 1
        
        for char in t:
            if char not in Container:
                return False
            else:
                Container[char] -= 1
                if Container[char] < 0:
                    return False
        return True