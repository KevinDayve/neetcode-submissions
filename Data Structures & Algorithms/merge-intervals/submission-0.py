class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals:
            lastInterval = merged[-1]
            if current[0] <= lastInterval[1]:
                lastInterval[1] = max(current[1], lastInterval[1])
            else:
                merged.append(current)
        return merged