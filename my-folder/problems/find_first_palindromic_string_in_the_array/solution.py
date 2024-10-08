class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(word):
            l=0
            r=len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        for c in words:
            if checkPalindrome(c):
                return c
        return ""