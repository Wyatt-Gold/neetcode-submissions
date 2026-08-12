class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        start_index = 0

        for end_index in range(0, len(s)):
            c = s[end_index]
            if c in seen:
                while s[start_index] != c:
                    seen.remove(s[start_index])
                    start_index += 1
                start_index += 1
            else:
                seen.add(c)
                longest = max(longest, end_index - start_index + 1)

        return longest