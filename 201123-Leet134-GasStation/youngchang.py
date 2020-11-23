class Solution:
    def canCompleteCircuit(self, gas, cost):        
        total = 0
        curr = 0
        answer = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                answer = i + 1
                curr = 0
        
        return answer if total_tank >= 0 else -1