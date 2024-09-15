class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix=0
        charMap=[0]*26
        charMap[ord('a')-ord('a')]=1
        charMap[ord('e')-ord('a')]=2
        charMap[ord('i')-ord('a')]=4
        charMap[ord('o')-ord('a')]=8 
        charMap[ord('u')-ord('a')]=16
        mp=[-1]*32
        ans=0
        for i,c in enumerate(s):
            prefix^=charMap[ord(c)-ord('a')]
            if mp[prefix]==-1 and prefix!=0:
                mp[prefix]=i
            ans=max(ans, i-mp[prefix])
        return ans