class Solution {
    public boolean isValid(String s) {
        Stack<Character> open = new Stack<Character>();
        for(char c : s.toCharArray()){
            switch(c){
                case '}':
                    if(open.isEmpty() || open.pop() != '{'){
                        return false;
                    }
                    break;
                case ']':
                    if(open.isEmpty() || open.pop() != '['){
                        return false;
                    }
                    break;
                case ')':
                    if(open.isEmpty() || open.pop() != '('){
                        return false;
                    }
                    break;
                default:
                    open.push(c);
                    break;
            }
        }

        return open.isEmpty() ? true : false;
    }
}
