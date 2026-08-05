class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> chars = new HashMap<Character, Integer>();
        int maxLength = 0;
        int currLength = 0;

        for(int i = 0; i < s.length(); i++){
            if(chars.containsKey(s.charAt(i))){
                maxLength = Math.max(maxLength, currLength);
                currLength = 0;
                i = chars.get(s.charAt(i));
                chars = new HashMap<Character, Integer>();
            } else {
                currLength++;
                chars.put(s.charAt(i), i);
            }
        }
        maxLength = Math.max(maxLength, currLength);

        return maxLength;
    }
}
