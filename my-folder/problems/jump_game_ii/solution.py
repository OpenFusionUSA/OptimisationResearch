class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        far=0
        ans=0
        while r<n-1:
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            ans+=1
        return ans