class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        midLen = len(s)/2
        sLen = len(s)
        for i in range(midLen):
            s[i], s[sLen - i - 1] = s[sLen - i - 1], s[i]

def testSolution():
    testCases = [
        {
            "input": ["h", "e", "l", "l", "o"],
            "output": ["o", "l", "l", "e", "h"]
        }
    ]
    
    solution = Solution()
    for testCase in testCases:
        solution.reverseString(testCase["input"])
        assert testCase["input"] == testCase["output"], "FAILED! Expected: {}, Got: {}".format(
            testCase["output"],
            testCase["input"]
        )

if __name__ == "__main__":
    testSolution()
