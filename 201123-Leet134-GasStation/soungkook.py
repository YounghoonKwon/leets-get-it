class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #완주
        #clock wise
        for i in range(len(gas)):
            current = i
            tank = 0
            for j in range(len(gas)):
                if i >= len(gas):
                    tank += gas[i - len(gas)]
                    tank = tank - cost[i - len(gas)]
                else:
                    tank += gas[i]
                    tank = tank - cost[i]
                
                   
                if tank < 0:
                    break
                    
                if j == len(gas)-1:
                    return current
                    
                i += 1
            
        return -1
