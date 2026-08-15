class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l < r:
            mid = l + (r-l)//2
            left_bound = nums[l]
            right_bound = nums[r]
            curr_num = nums[mid]

            if left_bound < curr_num and curr_num < right_bound:
                # In ascending order
                return left_bound
            elif left_bound < curr_num and curr_num > right_bound:
                # At local maximum
                l = mid + 1
                res = min(left_bound, right_bound)
            elif left_bound > curr_num and curr_num < right_bound:
                # At local minimum
                r = mid - 1
                res = min(res, curr_num)
            else:
                min_bounds = min(left_bound, right_bound)
                res = min(res, min_bounds)
                break

        return res