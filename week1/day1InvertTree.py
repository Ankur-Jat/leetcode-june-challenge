# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def bfs(root):
        result = []
        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def testSolution():
    solution = Solution()
    testCases = [
        {
            "input": None,
            "output": []
        },
        {
            "input": TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))),
            "output": [4,7,2,9,6,3,1]
        }
    ]
    for testCase in testCases:
        outputRoot = solution.invertTree(testCase["input"])
        output = TreeNode.bfs(outputRoot)
        assert testCase["output"] == output, "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)


if __name__ == "__main__":
    testSolution()