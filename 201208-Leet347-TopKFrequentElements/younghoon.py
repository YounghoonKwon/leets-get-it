class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = dict()
        for num in nums:
            num_set[num] = num_set.get(num,0) + 1
        num_set = sorted(num_set.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(num_set[i][0])
        
        return result
            
            
