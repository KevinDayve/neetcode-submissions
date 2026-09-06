class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Output = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in Output:
                Output[key] = []
            Output[key].append(word)
        return list(Output.values())