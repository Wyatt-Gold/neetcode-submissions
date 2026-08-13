class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s1) == 1:
            return s1 in s2
        
        s1_freqs = {}
        for c in s1:
            s1_freqs[c] = s1_freqs.get(c, 0) + 1
        
        s2_freqs = {}
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            s2_freqs[c] = s2_freqs.get(c, 0) + 1
            if c not in s1_freqs:
                s2_freqs = {}
                l = r + 1
                continue
            if r - l + 1 == len(s1):
                if len(s2_freqs) != len(s1_freqs):
                    s2_freqs[s2[l]] = s2_freqs[s2[l]] - 1
                    l += 1
                    continue
                even = True
                for key in s2_freqs:
                    if s2_freqs[key] != s1_freqs[key]:
                        s2_freqs[s2[l]] = s2_freqs[s2[l]] - 1
                        l += 1
                        even = False
                        break
                if even:
                    return True
        return False
