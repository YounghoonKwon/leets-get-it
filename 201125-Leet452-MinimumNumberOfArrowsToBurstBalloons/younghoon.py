import sys
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        boom = -sys.maxsize
        count = 0
        for i in range(len(points)):
            if points[i][0] <= boom:
                continue
            else:
                boom = points[i][1]
                count += 1
        return count
