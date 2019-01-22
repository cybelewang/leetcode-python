"""
134 Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

"""
# be sure to ask the case when len(gas) == 1
# similar to problem 53, maximum subarray
class Solution(object):
    # best solution
    # delta = gas - cost
    # if cannot circulate once for any start, the sum of the delta array must < 0, in this case, return -1
    # otherwise, there must be a start to complete the circuit, the last start with subarray's sum >=0 will meet this requirement
    # why last start meets the requirement? Because (1) sum of delta >0 (2) sum of delta[:start] must be the smallest negative (3) sum of delta[start:] > 0, and must be the biggest positive
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if n < 1:
            return -1

        start, leftGas, sum = 0, 0, 0
        for i in range(n):
            leftGas += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if sum < 0:
                sum = 0
                start = i + 1
        
        return -1 if leftGas < 0 else start


    # accepted, but seems not optimized because j iterates 2*n
    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if n < 1:
            return -1

        i, remain = 0, 0

        for j in range(1, 2*n): # think about another array following the original array, so we can go through a loop for start in any value from 0 to n-1
            remain += gas[(j - 1)%n] - cost[(j - 1)%n]
            if remain < 0:
                if j >= n:
                    return -1
                else:
                    i = j
                    remain = 0
            elif j%n == i:
                    return i
        
        return -1

obj = Solution()
gas = [4]
cost = [5]
print(obj.canCompleteCircuit(gas, cost))