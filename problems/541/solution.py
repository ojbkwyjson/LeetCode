import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, k = test_input
        return self.reverseStr(str(s), k)

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ''.join([s[i:i+k][::-1] if i % (2 * k) == 0 else s[i:i+k] for i in range(0, len(s), k)])
