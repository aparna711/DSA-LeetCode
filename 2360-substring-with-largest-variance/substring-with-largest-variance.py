class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
    # 148 Aparna Nair    
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        ans = 0

        for a in freq:
            for b in freq:
                if a == b:
                    continue
                countA = 0
                countB = 0
                remainingB = freq[b]

                for ch in s:
                    if ch == a:
                        countA += 1
                    elif ch == b:
                        countB += 1
                        remainingB -= 1
                    if countB > 0:
                        ans = max(ans, countA - countB)

                    if countB > countA and remainingB > 0:
                        countA = 0
                        countB = 0
        return ans