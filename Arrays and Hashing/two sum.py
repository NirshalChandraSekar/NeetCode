nums = [3,4,5,6]
target = 7
for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    if(nums[i] + nums[j] == target):
                        print([i,j])