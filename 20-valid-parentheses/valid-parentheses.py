class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch in '([{':
               stack.append(ch)
            else:
                if (not stack) or stack[-1] != brackets[ch]:
                 return False
                stack.pop()
        return len(stack) == 0