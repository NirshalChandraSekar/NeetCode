class Solution:
    max_value = 0
    def maximumTripletValue(self, nums):
        for i in range(len(nums-2)):
            for j in range(i+1, len(nums-1)):
                for k in range(j+1, len(nums-1)):
                    max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
        return max_value