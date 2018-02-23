numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return left + 1, right + 1
        return -1, -1


test_case = [
    ( [1,2,3,4,5,6,7,8], 5, [1,4] ),
    ( [2,7,11,15], 9, [1,2] ),
]


s = Solution()
for i in test_case:
    r = s.twoSum(i[0],i[1])
    print(r, r == i[2])