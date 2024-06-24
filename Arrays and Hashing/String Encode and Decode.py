class Solution:

    def encode(self, strs):
        output = ""
        for i in strs:
            output += i
            output += "niru"
        return output

    def decode(self, s):
        
        output = s.split("niru")
        output.pop()
        return output
    
        
if __name__ == '__main__':
    s = Solution()
    strs = ["neet","code","love","you"]
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))