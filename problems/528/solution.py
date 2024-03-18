import solution
from itertools import accumulate
from random import randint
from bisect import bisect_left


class Solution(solution.Solution):
    def solve(self, test_input=None):
        obj = RandomPick(test_input[1][0][0])
        ans = []
        for i in range(1, len(test_input[1])):
            ans.append(obj.pickIndex())
        return [None] + sorted(ans, reverse=True)


class RandomPick:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        # 计算前缀和，这样可以生成一个随机数，根据数的大小对应分布的坐标
        self.presum = list(accumulate(w))

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect_left(self.presum, randint(1, self.presum[-1]))