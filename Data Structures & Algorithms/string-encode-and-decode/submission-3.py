class Solution:
    seperator = '#'

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

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
