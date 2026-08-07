class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return str(x) == str(x)[: :-1]  
        
        new = str(x) 
        left = 0
        right = len((new)) - 1
        while left < right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True
         