class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n%2==0:
            return (n/2)+self.numberOfMatches(n/2)
        else:
            return (n-1)/2+self.numberOfMatches((n-1)/2+1)