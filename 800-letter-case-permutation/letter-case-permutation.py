class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 148 Aparna Nair
        res = [""]

        for ch in s:
            if ch.isalpha():
                res = [word + ch.lower() for word in res] + \
                      [word + ch.upper() for word in res]
            else:
                res = [word + ch for word in res]

        return res