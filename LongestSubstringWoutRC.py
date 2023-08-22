class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        st = ''
        '''
        p = ''
        for x in s:
            if st == '':
                st += x
                print("added")
                p = x
            elif x in s and x not in st:
                print("true")
                st += x
                p = x
            elif x in s and x in st and x == p:
                st = x
            else:
                print("false")
        '''

        list=[]

        for x in s:
            if x not in list:
                list.append(x)
                st += x
            elif x in list:
                list.append(x)
                i = list.pop()
                list.append(i)
        newst = ''
        if st not in s:
            list.pop(0)
            newst = st[1:]
            print(list)
            return len(newst)
        

            
        #print(list)
        #return st



s = "abcabcbb"
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = " "
sol = Solution()
sollen = sol.lengthOfLongestSubstring(s)
print(sollen)