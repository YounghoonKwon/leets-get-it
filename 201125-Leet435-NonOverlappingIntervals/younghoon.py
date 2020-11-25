import sys
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        close = -sys.maxsize
        intervals.sort(key = lambda x: x[1])
        count = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= close:
                close = intervals[i][1]
            else:
                count += 1
                
        return count
                    
