class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        na = [0] * len(nums)




        for i in range(len(nums)):
            multiplier = 1
            for k in range (len(nums)):
                if i != k:
                    multiplier *= nums[k]
                else:
                    continue
            na[i] = multiplier
            
        return na
