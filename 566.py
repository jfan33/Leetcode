# reshaping matrix

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = sum(nums, [])
        if len(flat) != r * c:
        return nums
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)

test_case = [
    ( [1,2,3,4,5,6,7,8], 5, [1,4] ),
    ( [2,7,11,15], 9, [1,2] ),
]

s=Solution()
