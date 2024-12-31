class Solution:
    def findDuplicate(self, nums):
        for num in nums:
            idx = abs(num)
            if nums[idx]<0:
                return abs(num)
            nums[idx] *= -1

if __name__ == "__main__":
    s = Solution()
    result = s.findDuplicate([1,3,4,2,2])
    print("Result:", result)

