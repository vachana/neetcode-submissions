class Solution {
    public boolean isValid(String s) {
        Stack<Character>stack = new Stack<>();

        for (char c: s.toCharArray()){
            if(!stack.isEmpty()) {
                if((c == '}' && stack.peek() == '{')
                || (c == ')' && stack.peek() == '(') 
                || (c == ']' && stack.peek() == '[')){
                         stack.pop();
                         continue;
                }
            
            }
            stack.push(c);
        }
        return stack.empty();
        
    }
}
