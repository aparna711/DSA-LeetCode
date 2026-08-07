from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
      
        scret_count = Counter(secret)
        guess_count = Counter(guess)


        bulls = sum(s == g for s,g in zip(secret, guess))
        total_matches = sum(min(scret_count[digit], guess_count[digit]) for digit in scret_count)
        cows = total_matches - bulls

           
        return str(bulls) + 'A'+ str(cows)+'B'
            
            