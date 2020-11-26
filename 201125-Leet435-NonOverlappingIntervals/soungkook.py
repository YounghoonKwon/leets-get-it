class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda data:(data[0], data[1]))
        output = 0
        fp = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[fp][1]:
                if intervals[i][1] < intervals[fp][1]:
                    fp = i
                output+=1
                continue
            fp = i
        return output
