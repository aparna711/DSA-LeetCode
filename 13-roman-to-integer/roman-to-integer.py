class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,     
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total_num = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total_num -= roman_dict[s[i]]
            else:
                total_num += roman_dict[s[i]]
        return total_num
        
    

            

