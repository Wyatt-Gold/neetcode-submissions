class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        for letter in s:
            if letter in sLetters:
                sLetters[letter] += 1
            else:
                sLetters[letter] = 1
        
        tLetters = {}
        for letter in t:
            if letter in tLetters:
                tLetters[letter] += 1
            else:
                tLetters[letter] = 1

        if len(sLetters) != len(tLetters):
            return False

        for key in tLetters:
            if key not in sLetters or sLetters[key] != tLetters[key]:
                return False
        
        return True