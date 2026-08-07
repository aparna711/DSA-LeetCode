class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return str(x) == str(x)[: :-1]  
        new = str(x)
        if new == new[::-1]:
            return True
        else:
            return False