class Solution:
    def twoSum(self, numbers, target):
        j = len(numbers)-1
        i = 0
        while i<j:
            if(numbers[i]+numbers[j] == target):
                return [i+1, j+1]
            elif(numbers[i]+numbers[j] < target):
                i += 1
            else:
                j -= 1

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9)) #Output: [1,2]
    print(s.twoSum([2,3,4], 6)) #Output: [1,3]
    print(s.twoSum([-1,0], -1)) #Output: [1,2]