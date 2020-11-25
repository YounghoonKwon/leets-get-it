class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        res = 1
        cur = points[0][1]
        for p in points[1:]:
            if cur < p[0]:
                res += 1
                cur = p[1]
        return res
