class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = -1
        cur = 0
        
        if sum(gas) < sum(cost):
            return -1;
        
        for i in range(len(gas)):
            if start == -1 and gas[i] < cost[i]:
                continue
            elif start == -1 and gas[i] >= cost[i]:
                start = i
            cur += gas[i]-cost[i]
            if cur < 0:
                start = i+1
                cur = 0
        return start
            
