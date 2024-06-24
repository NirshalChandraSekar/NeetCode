class Solution:
    def __init__(self):
        self.table = {}

    def topKFrequent(self, nums, k):
        for i in nums:
            key, value = i, i
            self.hashtable(key,value)    

        sorted_items = sorted(self.table.items(), key=lambda x: len(x[1]), reverse=True)
        output = []
        for i in range(k):
            output.append(sorted_items[i][0])
        
        return output

    def hashtable(self, key, value):
        if(key in self.table):
            self.table[key].append(value)
        else:
            self.table[key] = [value]
        
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    output = sol.topKFrequent(nums, k)
    print(output)