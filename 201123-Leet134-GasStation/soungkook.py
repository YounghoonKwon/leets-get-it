class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #완주
        #clock wise
        for i in range(len(gas)):
            tank = 0
            for j in range(i, i + (len(gas))):
                idx = j
                
                if j >= len(gas):
                    idx = j - (len(gas))
                
                tank += gas[idx]
                tank -= cost[idx]
                
                if tank < 0:
                    break
                
                if j == i + len(gas) - 1:
                    return i
            
        return -1
