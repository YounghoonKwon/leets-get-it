class Solution(object):
    def findMinArrowShots(self, points):   
        if len(points) < 2:
            return len(points)

        points.sort(key = lambda x: x[0])
        count = 1

        end = points[0][1]
        for i in range(1, len(points)):
            if end >= points[i][0]:
                end = min(points[i][1], end)
            else:
                end = points[i][1]
                count += 1
        return count
