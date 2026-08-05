class Solution {
    public String minWindow(String s, String t) {
        String res = "";

        Map<Character, Integer> map = new HashMap<>();
        for(char c : t.toCharArray()){
            Integer count = map.get(c);
            if(count == null){
                count = 0;
            }
            map.put(c, count + 1);
        }

        int startIndex = 0;
        int minLength = s.length() + 1;
        int letterCount = 0;
        for(int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            if(map.containsKey(curr)){
                int count = map.get(curr);
                count--;
                map.put(curr, count);
                if(count >= 0){
                    letterCount++;
                    if(letterCount == t.length()){
                        while(startIndex <= i && letterCount == t.length()){
                            char remove = s.charAt(startIndex);
                            if(map.containsKey(remove)){
                                int tempCount = map.get(remove);
                                if(tempCount == 0){
                                    letterCount--;
                                    if((i - startIndex) + 1 < minLength){
                                        minLength = (i - startIndex) + 1;
                                        res = s.substring(startIndex, i + 1);
                                    }
                                }
                                tempCount++;
                                map.put(remove, tempCount);
                            }
                            startIndex++;
                        }
                    }
                }
            }
        }

        return res;
    }
}
