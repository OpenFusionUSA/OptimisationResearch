class Solution {
    //step 1
    int cnt = 0;
    public int findTargetSumWays(int[] nums, int target) {
        //step 2
        DFS(nums, 0, 0, target);
        //step 5
        return cnt;
    }

    private void DFS(int[] nums, int index, int sum, int target) {
        //step 3
        if (index == nums.length) {
            if (sum == target) cnt++;
            return;
        }
        //step 4
        DFS(nums, index + 1, sum + nums[index], target);
        DFS(nums, index + 1, sum - nums[index], target);
    }
}