class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        List<String> strings = new ArrayList<>(Arrays.asList(strs));

        List<String> anagrams;
        while(strings.size() > 0){
            String currWord = strings.remove(0);
            anagrams = new ArrayList<String>();
            anagrams.add(currWord);
            for(int i = 0; i < strings.size(); i++){
                if(anagrams(currWord, strings.get(i))){
                    anagrams.add(strings.get(i));
                    strings.remove(i);
                    i--;
                }
            }
            ans.add(anagrams);
        }

        return ans;
    }

    public boolean anagrams(String str1, String str2){
        if(str1.length() != str2.length()){
            return false;
        }

        Hashtable<Character, Integer> freqs1 = new Hashtable<Character, Integer>();
        Hashtable<Character, Integer> freqs2 = new Hashtable<Character, Integer>();
        for(int i = 0; i < str1.length(); i++){
            Integer freq = freqs1.get(str1.charAt(i));
            if(freq == null){
                freq = 0;
            }
            freqs1.put(str1.charAt(i), freq + 1);

            freq = freqs2.get(str2.charAt(i));
            if(freq == null){
                freq = 0;
            }
            freqs2.put(str2.charAt(i), freq + 1);
        }

        for(Character letter : freqs1.keySet()){
            if(!freqs2.containsKey(letter) || !freqs1.get(letter).equals(freqs2.get(letter))){
                return false;
            }
        }

        return true;
    }
}
