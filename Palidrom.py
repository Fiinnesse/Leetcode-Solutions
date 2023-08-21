x = 121
#str = ''

class Solution:

    def __init__(self) -> None:
        self.str = str

    def isPalindrome(self, x: int) -> bool:
        org = ''
        rev = ''
        for j in str(x):
            #print(j)
            org += j
        #print(org)
        for i in reversed(str(x)):
            rev += i
            #print(i)
        #print(rev)
        if rev == org:
            return True
        else:
            return False
        

print(Solution.isPalindrome(str, x))