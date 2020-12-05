class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        last_arrow = -float('inf')

        answer = 0

        for point in points:
            if last_arrow < point[0]:
                answer += 1
                last_arrow = point[1]

        return answer