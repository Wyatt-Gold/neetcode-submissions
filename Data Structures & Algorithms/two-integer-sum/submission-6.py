class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in prevNums:
                return [prevNums[temp], i]
            prevNums[nums[i]] = i
        return [0, 0]