class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0
        j = 1

        while i <= len(nums) - 3:
            temp = self.twoSum(nums, j, nums[i] * -1)
            while temp is not None:
                res.append([nums[i], nums[temp[0]], nums[temp[1]]])
                j = temp[0] + 1
                while nums[j] == nums[j-1] and j <= len(nums) - 2:
                    j += 1
                temp = self.twoSum(nums, j, nums[i] * -1)
            
            i += 1
            while nums[i] == nums[i-1] and i <= len(nums) - 3:
                i += 1
            j = i + 1
        
        return res
    
    def twoSum(self, nums: List[int], start: int, target: int):
        if start >= len(nums) - 1:
            return None

        index1 = start
        index2 = len(nums) - 1

        while nums[index1] + nums[index2] != target and index1 < index2:
            if nums[index1] + nums[index2] < target:
                index1 += 1
            else:
                index2 -= 1
        
        if index1 >= index2:
            return None
        return [index1, index2]

