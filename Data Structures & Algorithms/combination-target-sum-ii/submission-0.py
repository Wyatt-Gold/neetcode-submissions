class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, curr_nums, remaining):
            if remaining <= 0:
                if remaining == 0:
                    res.append(curr_nums.copy())
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_nums.append(candidates[i])
                backtrack(i+1, curr_nums, remaining - candidates[i])
                curr_nums.pop()
            
        backtrack(0, [], target)
        return res