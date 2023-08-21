s = "MCMXCIV"
num = 0
roman_dict = {'I':1, 'V':5 ,'X': 10,'L' :50 , 'C':100, 'D':500, 'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        i = n-1
        total = 0

        while i >= 0:
            #print(roman_dict[s[i]])
            
            if i < n-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]]
            i -= 1
        return total
            


print(Solution.romanToInt(num, s))

