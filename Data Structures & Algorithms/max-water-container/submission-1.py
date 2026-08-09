class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = min(heights[i], heights[j]) * (j - i)

        while i < j:
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            res = max(res, (min(heights[i], heights[j]) * (j - i)))

        return res
