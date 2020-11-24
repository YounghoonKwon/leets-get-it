class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        @lru_cache(None)
        def recur(idx, down):
            if idx == N:
                return 1
            curr = nums[idx]
            res = 0
            if down:
                for i in range(idx + 1, N):
                    if curr < nums[i]:
                        res = max(res, recur(i, False))
            else:
                for i in range(idx + 1, N):
                    if curr > nums[i]:
                        res = max(res, recur(i, True))
                    
            return res + 1
        answer = -float('inf')
        for i in range(N):
            answer = max(answer, recur(i, True))
            answer = max(answer, recur(i, False))
        return answer