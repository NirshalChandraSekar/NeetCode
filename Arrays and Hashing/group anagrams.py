class Solution:
    def __init__(self):
        self.table = {}
    def groupAnagrams(self, strs):
        for i in strs:
            key = list(i)
            key.sort()
            keystr = ''.join([str(elem) for elem in key])
            self.hashtable(keystr, i)
        
        output = []
        for k in self.table:
            output.append(self.table[k])
        
        return output

    
    def hashtable(self, key, value):
        if(key in self.table):
            self.table[key].append(value)
        else:
            self.table[key] = [value]

# write a main function to test the code
# should be __init__

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    