class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        st =  ''
        for x in s[1::]:
            if x not in st:
            
                st += x

        return len(st)



s = "abcabcbb"
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = " "
sol = Solution()
sollen = sol.lengthOfLongestSubstring(s4)
print(sollen)