class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> s_nums = new HashSet<>();
        for (int n: nums) s_nums.add(n);
        return s_nums.size() != nums.length;
    }
}