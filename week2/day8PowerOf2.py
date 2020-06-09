class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (n-1) == 0


def testSolution():
    testCases = [
            {
                "input": 0,
                "output": False
            },
            {
                "input": 1,
                "output": True,
            },
            {
                "input": 1024,
                "output": True
            },
            {
                "input": 13,
                "output": False,
            }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.isPowerOfTwo(testCase["input"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)


if __name__ == "__main__":
    testSolution()

