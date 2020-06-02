"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        temp = node.next
        node.next = temp.next
        # This will ensure no dangling object reference.
        if temp.next:
            temp.next = None

def testSolution():
    def makeListNode(nodes):
        head = None
        ptr = None
        while nodes:
            node = ListNode(nodes.pop(0))
            if head:
                ptr.next, ptr = node, node
            else:
                head, ptr = node, node
        return head

    testCases = [
        {
            "list": makeListNode([4,5,1,9]),
            "input": 2,
            "output": [4,5,9] 
        },
        {
            "list": makeListNode([4,5,1,9]),
            "input": 1,
            "output": [4,1,9]
        },
    ]

    solution = Solution()
    for testCase in testCases:
        counter = 0
        node = testCase["list"]
        while counter < testCase["input"]:
            node = node.next
            counter += 1
        solution.deleteNode(node)
        output = []
        node = testCase["list"]
        while node:
            output.append(node.val)
            node = node.next
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)

if __name__ == "__main__":
    testSolution()
