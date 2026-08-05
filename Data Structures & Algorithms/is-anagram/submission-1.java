class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        Hashtable<Character, Integer> letters1 = new Hashtable<>();
        Hashtable<Character, Integer> letters2 = new Hashtable<>();

        for(int i = 0; i < s.length(); i++){
            int val1 = 0;
            if(letters1.containsKey(s.charAt(i))){
                val1 = letters1.get(s.charAt(i));
            }
            letters1.put(s.charAt(i), val1 + 1);


            int val2 = 0;
            if(letters2.containsKey(t.charAt(i))){
                val2 = letters2.get(t.charAt(i));
            }
            letters2.put(t.charAt(i), val2 + 1);
        }

        if(letters1.size() != letters2.size()){
            return false;
        }

        for(Character key : letters1.keySet()){
            if(!letters2.containsKey(key) || !letters2.get(key).equals(letters1.get(key))){
                return false;
            }
        }

        return true;
    }
}
