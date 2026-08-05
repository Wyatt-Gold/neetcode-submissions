class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sLetters, tLetters = {}, {}
        for i in range(len(s)):
            sLetters[s[i]] = 1 + sLetters.get(s[i], 0)
            tLetters[t[i]] = 1 + tLetters.get(t[i], 0)

        return sLetters == tLetters