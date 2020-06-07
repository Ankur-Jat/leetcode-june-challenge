class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for amt in xrange(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        return dp[-1]


def testSolution():
    testCases = [
        {
            "input": {
                "amount": 6,
                "coins": [2, 3, 5]
            },
            "output": 2
        }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.change(testCase["input"]["amount"], testCase["input"]["coins"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)


if __name__ == "__main__":
    testSolution()