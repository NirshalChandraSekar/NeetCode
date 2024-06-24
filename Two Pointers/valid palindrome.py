class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "")
        string = string.lower()
        string = filter(str.isalnum, string)
        string = "".join(string)
        string2 = string[::-1]
        if(string != string2):
            return False
        else:
            return True
        
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Was it a car or a cat I saw?"))