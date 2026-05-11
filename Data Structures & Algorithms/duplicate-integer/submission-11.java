class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Set<Integer> s_nums = new HashSet<>();
        // for (int n: nums) s_nums.add(n);
        // return s_nums.size() != nums.length;

        Set<Integer> s_nums = new HashSet<>();

        for(int i=0;i < nums.length; i++) {
            if (!s_nums.add(nums[i]))
                return true;
            
        }
        return false;
    }

}