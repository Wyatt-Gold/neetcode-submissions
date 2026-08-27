class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, curr_list):
            res.append(curr_list.copy())

            for i in range(start, n):
                curr_list.append(nums[i])
                backtrack(i + 1, curr_list)
                curr_list.pop()

        backtrack(0, [])
        return res