class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sStart = 0
        tStart = 0
        matchingCharCount = 0
        while sStart < len(s) and tStart < len(t):
            if s[sStart] == t[tStart]:
                matchingCharCount += 1
                sStart += 1
                tStart += 1
            else:
                tStart += 1
        return matchingCharCount == len(s)

def testSolution():
    testCases = [
            {
                "input": {
                    "s": "abc",
                    "t": "ahbgdc"
                },
                "output": True
            },
            {
                "input": {
                    "s": "axc",
                    "t": "ahbgdc"
                },
                "output": False
            }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.isSubsequence(testCase["input"]["s"], testCase["input"]["t"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)


if __name__ == "__main__":
    testSolution()
