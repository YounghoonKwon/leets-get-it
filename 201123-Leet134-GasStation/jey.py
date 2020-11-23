class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: return -1
        tank = 0
        start = 0
        total = 0 # accumulate total cost gas
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1 # reset start only when tank < 0
                total += tank
                tank = 0
        if tank + total < 0:
            return -1
        else:
            return start     
