class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = {}
        leftProducts[0] = 1
        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]

        rightProducts = {}
        rightProducts[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(leftProducts[i] * rightProducts[i])
        
        return res