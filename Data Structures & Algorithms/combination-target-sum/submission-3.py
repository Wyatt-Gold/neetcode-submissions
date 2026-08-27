class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, curr_nums, remaining):
            if remaining <= 0:
                if remaining == 0:
                    res.append(curr_nums.copy())
                return
            
            for i in range(start, n):
                curr_nums.append(nums[i])
                backtrack(i, curr_nums, remaining - nums[i])
                curr_nums.pop()
            
        backtrack(0, [], target)
        return res