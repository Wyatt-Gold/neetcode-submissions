class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_length = 0
        start_index = 0
        max_freq = 0
        

        for end_index in range (len(s)):
            c = s[end_index]
            freqs[c] = freqs.get(c, 0) + 1
            max_freq = max(max_freq, freqs[c])
            if(end_index - start_index + 1 - max_freq > k):
                while s[start_index] == c:
                    freqs[s[start_index]] = freqs[s[start_index]] - 1
                    start_index += 1
                freqs[s[start_index]] = freqs[s[start_index]] - 1
                max_freq = max(max_freq, freqs[s[start_index]])
                start_index += 1
            max_freq = max(max_freq, freqs[c])
            max_length = max(max_length, end_index - start_index + 1)

        return max_length

            
