class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        for num in nums:
            if num not in Counter:
                Counter[num] = 1
            else:
                Counter[num] += 1
        return sorted(Counter, key=Counter.get, reverse=True)[:k]