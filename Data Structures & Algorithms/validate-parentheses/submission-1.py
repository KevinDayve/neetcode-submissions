class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combinations = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for char in s:
            if char in combinations:
                stack.append(char)
            else:
                if not stack or combinations[stack[-1]] != char:
                    return False
                stack.pop()
        return not stack