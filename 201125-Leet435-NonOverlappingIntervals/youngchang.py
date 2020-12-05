class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda x: (x[1], -x[0]))
        stack = [intervals[0]]
        answer = 0
        for i in range(1, len(intervals)):
            prev = stack[-1]
            curr = intervals[i]
            if prev[1] > curr[0]:
                answer += 1
            else:
                stack.append(curr)
        return answer