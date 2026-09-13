class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currInterval = intervals[0]

        nonOverlap = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= currInterval[1]:
                currInterval = [currInterval[0], max(intervals[i][1], currInterval[1])]
            else:
                nonOverlap.append(currInterval)
                currInterval = intervals[i]
        
        nonOverlap.append(currInterval)
        return nonOverlap