class Solution: 
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        counter = Counter(nums)
        tails = Counter()
        
        for n in nums:
            if not counter[n]: continue
            elif tails[n] > 0:
                tails[n] -= 1
                tails[n + 1] += 1
            elif counter[n + 1] > 0 and counter[n + 2] > 0:
                counter[n + 1] -= 1
                counter[n + 2] -= 1
                tails[n + 3] += 1
            else: return False
            counter[n] -= 1
        return True
