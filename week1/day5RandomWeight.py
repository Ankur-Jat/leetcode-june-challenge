import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.wCopy = []
        self.totalSum = sum(self.w)
        self.totalSumCopy = sum(self.wCopy)

    def pickIndex(self):
        """
        :rtype: int
        """
        if not self.totalSumCopy:
            self.wCopy = self.w[:]
            self.totalSumCopy = self.totalSum
        randomIndex = random.randrange(0, self.totalSumCopy)
        for (index, item) in enumerate(self.wCopy):
            if item <= randomIndex:
                randomIndex -= item
                continue
            self.totalSumCopy -= 1
            self.wCopy[index] -= 1
            return index
        return len(self.wCopy) - 1


solution = Solution([1, 2])
itemCount = {}
for _ in range(1000000):
    item = solution.pickIndex()
    if itemCount.get(item, None) == None:
        itemCount[item] = 1
    else:
        itemCount[item] += 1
print itemCount

