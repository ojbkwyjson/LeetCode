import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        candiesCount, queries = test_input
        return self.canEat(list(candiesCount), [x[:] for x in queries])

    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(candiesCount)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + candiesCount[i]
        ans = []
        for c_type, day, daily in queries:
            if presum[c_type] // daily <= day < presum[c_type + 1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans