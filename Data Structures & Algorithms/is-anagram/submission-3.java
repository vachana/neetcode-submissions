class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        
        Map<Character, Integer>s_count = new HashMap<>();
        Map<Character, Integer>t_count = new HashMap<>();

        for(char c: s.toCharArray()) {
            s_count.put(c, s_count.getOrDefault(c, 0) + 1);
        }
        
        for(char c: t.toCharArray()) {
            t_count.put(c, t_count.getOrDefault(c, 0) +1);
        }

        return t_count.equals(s_count);
    }
}
