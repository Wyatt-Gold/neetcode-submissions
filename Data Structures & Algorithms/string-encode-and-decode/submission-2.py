class Solution:
    seperator = '#'

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += self.seperator
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        prevIndex = 0;
        currIndex = 1;
        while currIndex < len(s):
            if s[currIndex] == self.seperator:
                length = int(s[prevIndex:currIndex])
                currIndex += 1
                res.append(s[currIndex:currIndex+length])
                currIndex += length
                prevIndex = currIndex
            currIndex += 1

        return res
