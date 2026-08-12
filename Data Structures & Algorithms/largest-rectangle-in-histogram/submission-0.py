class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append([heights[0], 0])
        max_area = heights[0] * 1

        for i in range(1, len(heights)):
            curr_height = heights[i]
            if stack and stack[-1][0] < curr_height:
                stack.append([curr_height, i])
            else:
                info = [curr_height, i]
                while stack and stack[-1][0] > curr_height:
                    info = stack.pop()
                    new_area = info[0] * (i - info[1])
                    max_area = max(max_area, new_area)
                stack.append([curr_height, info[1]])
        
        while stack:
            info = stack.pop()
            new_area = info[0] * (len(heights) - info[1])
            max_area = max(max_area, new_area)
        
        return max_area
