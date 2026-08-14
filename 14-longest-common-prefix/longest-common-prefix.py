class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        strs = strs[1:]
        for word in strs:
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[0:i]
    
        return prefix
'''
        prefix = strs[0]
        strs = strs[1:]
        for word in strs:
            i = 0
            while i<len(prefix) and i<len(strs) and prefix[i] == word[i]:
              i += 1  
            prefix = prefix[0:i]
        
        return prefix
'''

   

        