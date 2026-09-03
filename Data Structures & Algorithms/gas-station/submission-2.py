class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = -1
        n = len(gas)
        index,tank = 0,0
        total_gas = 0
        total_cost = 0
        #starting index  = i
        for i in range(n):
            x = i%n
            tank += gas[x] - cost[x]
            if tank < 0:
                index = i+1
                tank = 0
            total_gas+=gas[x]
            total_cost+=cost[x]
            
        if total_gas>=total_cost:
            return index
        return -1
