class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        
        n, start, wallet = len(gas), 0, 0
        for i in range(n):
            wallet += gas[i] - cost[i]
            if wallet < 0:
                start, wallet = i+1, 0
        return start
            
