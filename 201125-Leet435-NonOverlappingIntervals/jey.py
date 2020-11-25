class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals)
        lastx, lasty = intervals[0]
        s, res = 1, 0
        while s < len(intervals):

            if lastx <= intervals[s][0] < lasty and intervals[s][-1] >= lasty:
               
                res += 1
                s += 1
                continue
     
            elif lastx <= intervals[s][0] < lasty and intervals[s][-1] <= lasty:
                res += 1
            # No overlap at all
            lastx, lasty = intervals[s]
            s += 1
        return res
