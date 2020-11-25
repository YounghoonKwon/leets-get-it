class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key= lambda x: x[1])
        count = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                count += 1
            else:
                prev = intervals[i][1]
        return count
