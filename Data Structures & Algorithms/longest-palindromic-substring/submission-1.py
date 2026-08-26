class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        res = s[0]

        for i in range(1, len(s)):
            l,r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - (l + 1):
                res = s[l+1: r]
            
            l,r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - (l + 1):
                res = s[l+1: r]

        return res