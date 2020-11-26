class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        left = 0
        right = 1
        size = len(intervals)
        count = 0
        while right < size:
            # overlap
            #overlap case : left bigger, within
            if intervals[left][1] > intervals[right][1]:
                left = right
                right +=1
                count +=1
            elif intervals[left][1] <= intervals[right][1]:
                # no overlap
                if intervals[left][1] <= intervals[right][0]:
                    left=right
                    right+=1
                #overlap case : right bigger or at least reached further out of left range
                else:
                    right += 1
                    count += 1
        return count
        
