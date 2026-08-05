class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();

        int start = 0;
        int end = s.length() - 1;
        
        while(start <= end){
            while(start < s.length() && !((s.charAt(start) >= 97 && s.charAt(start) <= 122) || (s.charAt(start) >= 48 && s.charAt(start) <= 57))){
                start++;
            }
            while(end >= 0 && !((s.charAt(end) >= 97 && s.charAt(end) <= 122) || (s.charAt(end) >= 48 && s.charAt(end) <= 57))){
                end--;
            }

            if(start > end){
                break;
            }

            if(s.charAt(start) != s.charAt(end)){
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
