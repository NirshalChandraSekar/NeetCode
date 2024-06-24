import math

class Solution:
    def productExceptSelf(self, nums):
        output = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            output.append(math.prod(temp))
        return output
    
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))