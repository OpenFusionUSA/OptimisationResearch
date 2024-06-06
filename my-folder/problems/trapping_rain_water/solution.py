class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        ans=0
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        left_max[0],right_max[-1]=height[0],height[-1]
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i])
            right_max[len(height)-1-i]=max(right_max[len(height)-i],height[len(height)-1-i])
        for i in range(len(height)):
            ans+=min(left_max[i],right_max[i])-height[i]
        return ans