class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        st = 0
        ed = len(height) - 1
        while st < ed:
            h = min(height[st], height[ed])
            w = ed - st
            answer = max(answer, h * w)
            if height[st] > height[ed]:
                ed -= 1
            else:
                st += 1
        return answer