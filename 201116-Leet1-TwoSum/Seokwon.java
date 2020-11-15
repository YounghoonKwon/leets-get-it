class Solution {
    int SIZE = 2;
    public int[] twoSum(int[] nums, int target) {
        int sum, i = 0;
        int[] reValue = new int[SIZE];
        while(i != nums.length-1){
            for(int j=i+1;j<nums.length;j++){
                sum = nums[i] + nums[j];
                if(sum == target){
                    reValue[0] = i;
                    reValue[1] = j;   
                }
            }
            i++;
        }
           return reValue;
    }
}
