class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=0
        ans=[0]*len(nums)
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                ans[p]=nums[i]
                p+=2
            else:
                ans[n]=nums[i]
                n+=2
        return ans