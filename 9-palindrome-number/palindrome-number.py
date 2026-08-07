class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Method 1 : Slicing
        # return str(x) == str(x)[: :-1]  
        
        # Method 2: Two Pointers
        new = str(x) 
        left = 0
        right = len((new)) - 1
        while left < right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True

       
         