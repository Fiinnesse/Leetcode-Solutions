class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        map = {}
        i = 0
        cur = 0
        llen = 0

        for x,y in enumerate(s):
            if y in map and map[y] >= i:
                i = map[y] + 1
                cur = x - map[y]
                map[y] = x
            else:
                map[y] = x
                cur += 1
                if cur > llen:
                    llen = cur
            
        return(llen)




s = "abcabcbb"
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = " "
sol = Solution()
sollen = sol.lengthOfLongestSubstring(s4)
print(sollen)