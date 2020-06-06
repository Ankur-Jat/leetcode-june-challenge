class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        ans=[]
        for p in people:
            ans.insert(p[1], p)
        return ans


def testSolution():
    testCases = [
        {
            "input": [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            "output": [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        },
        {
            "input": [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]],
            "output": [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
        },
        {
            "input": [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]],
            "output": [[6, 0], [1, 1], [8, 0], [7, 1], [9, 0], [2, 4], [0, 6], [2, 5], [3, 4], [7, 3]]
        },
        {
            "input": [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]],
            "output": [[0,0],[6,0],[1,1],[5,1],[5,2],[4,3],[7,0],[6,2],[5,5],[6,3]]
        }
    ]

    solution = Solution()
    for (index, testCase) in enumerate(testCases):
        output = solution.reconstructQueue(testCase["input"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)


testSolution()