class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        total = 0

        i = len(cost) - 1

        while i >= 0:
            total += cost[i]
            if i - 1 >= 0:
                total += cost[i - 1]

            i -= 3

        return total
        
        

        
        